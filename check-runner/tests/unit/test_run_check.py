"""Tests for run_check_async function."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from check_runner import run_check_async


def _make_pool_and_conn():
    """Returns (mock_pool, mock_conn) wired for asyncpg pool.acquire() usage.

    asyncpg's pool.acquire() and conn.transaction() are called synchronously
    and return async context managers — they must NOT be AsyncMock themselves.
    """
    mock_conn = AsyncMock()

    # conn.transaction() → sync call → async context manager
    mock_transaction_cm = MagicMock()
    mock_transaction_cm.__aenter__ = AsyncMock(return_value=None)
    mock_transaction_cm.__aexit__ = AsyncMock(return_value=False)
    mock_conn.transaction = MagicMock(return_value=mock_transaction_cm)

    # pool.acquire() → sync call → async context manager yielding mock_conn
    mock_acquire_cm = MagicMock()
    mock_acquire_cm.__aenter__ = AsyncMock(return_value=mock_conn)
    mock_acquire_cm.__aexit__ = AsyncMock(return_value=False)

    mock_pool = MagicMock()
    mock_pool.acquire = MagicMock(return_value=mock_acquire_cm)
    return mock_pool, mock_conn


async def test_run_check_async_single_stage():
    mock_pool, mock_conn = _make_pool_and_conn()
    mock_conn.fetch.return_value = [{"col": 1}, {"col": 2}, {"col": 3}]

    stages = [("01_select.sql", "SELECT * FROM test")]
    result = await run_check_async(mock_pool, "my_check", stages, {})

    assert result == {"check": "my_check", "status": "ok", "rows": 3, "stages": 1}
    mock_conn.fetch.assert_called_once()


async def test_run_check_async_multiple_stages():
    mock_pool, mock_conn = _make_pool_and_conn()
    mock_conn.execute.return_value = "DELETE 5"
    mock_conn.fetch.return_value = [{"col": 1}]

    stages = [
        ("01_cleanup.sql", "DELETE FROM old"),
        ("02_insert.sql", "INSERT INTO new VALUES (1)"),
        ("03_select.sql", "SELECT * FROM new"),
    ]
    result = await run_check_async(mock_pool, "my_check", stages, {})

    assert result["stages"] == 3
    assert result["rows"] == 11  # 5 (DELETE) + 5 (INSERT, which also returns DELETE status) + 1 (SELECT)
    assert result["status"] == "ok"


async def test_run_check_async_dml_counts_status_number():
    mock_pool, mock_conn = _make_pool_and_conn()
    mock_conn.execute.return_value = "DELETE 7"

    stages = [("01_delete.sql", "DELETE FROM old WHERE id = %(id)s")]
    result = await run_check_async(mock_pool, "my_check", stages, {"id": 42})

    assert result == {"check": "my_check", "status": "ok", "rows": 7, "stages": 1}


async def test_run_check_async_with_named_params():
    mock_pool, mock_conn = _make_pool_and_conn()
    mock_conn.fetch.return_value = [{"id": 1}]

    stages = [("01_q.sql", "SELECT * FROM devices WHERE id = %(device_id)s")]
    result = await run_check_async(mock_pool, "my_check", stages, {"device_id": "abc"})

    assert result["status"] == "ok"
    call_args = mock_conn.fetch.call_args
    # Named param %(device_id)s must be converted to positional $1
    assert "$1" in call_args[0][0]
    assert "abc" in call_args[0]


async def test_run_check_async_missing_param_raises():
    mock_pool, mock_conn = _make_pool_and_conn()

    stages = [("01_q.sql", "SELECT * FROM devices WHERE id = %(missing_param)s")]
    with pytest.raises(KeyError, match="missing_param"):
        await run_check_async(mock_pool, "my_check", stages, {})


async def test_run_check_async_no_results():
    mock_pool, mock_conn = _make_pool_and_conn()
    mock_conn.execute.return_value = "INSERT 0 0"

    stages = [("01_insert.sql", "INSERT INTO test VALUES (1)")]
    result = await run_check_async(mock_pool, "my_check", stages, {})

    assert result == {"check": "my_check", "status": "ok", "rows": 0, "stages": 1}


async def test_run_check_async_empty_select_results():
    mock_pool, mock_conn = _make_pool_and_conn()
    mock_conn.fetch.return_value = []

    stages = [("01_select.sql", "SELECT * FROM test WHERE 1=0")]
    result = await run_check_async(mock_pool, "my_check", stages, {})

    assert result == {"check": "my_check", "status": "ok", "rows": 0, "stages": 1}


async def test_run_check_async_unparseable_dml_status():
    """execute() returning a non-standard status string doesn't crash row counting."""
    mock_pool, mock_conn = _make_pool_and_conn()
    mock_conn.execute.return_value = "OK"

    stages = [("01_d.sql", "DELETE FROM t")]
    result = await run_check_async(mock_pool, "my_check", stages, {})

    assert result["status"] == "ok"
    assert result["rows"] == 0
