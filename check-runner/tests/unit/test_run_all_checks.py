"""Tests for concurrent check execution (via run_once_async)."""

from unittest.mock import AsyncMock, MagicMock, patch

from check_runner import run_once_async


def _make_pool(fetch_return=None, execute_return="INSERT 0 1"):
    """Build a minimal asyncpg pool mock that returns mock_conn on acquire.

    pool.acquire() and conn.transaction() must be sync calls returning async
    context managers — they must NOT be AsyncMock themselves.
    Returns (pool_acm, mock_pool, mock_conn) where pool_acm is the object
    returned by asyncpg.create_pool() (an async context manager wrapping pool).
    """
    mock_conn = AsyncMock()
    mock_conn.fetch.return_value = fetch_return if fetch_return is not None else []
    mock_conn.execute.return_value = execute_return

    mock_transaction_cm = MagicMock()
    mock_transaction_cm.__aenter__ = AsyncMock(return_value=None)
    mock_transaction_cm.__aexit__ = AsyncMock(return_value=False)
    mock_conn.transaction = MagicMock(return_value=mock_transaction_cm)

    mock_acquire_cm = MagicMock()
    mock_acquire_cm.__aenter__ = AsyncMock(return_value=mock_conn)
    mock_acquire_cm.__aexit__ = AsyncMock(return_value=False)

    mock_pool = MagicMock()
    mock_pool.acquire = MagicMock(return_value=mock_acquire_cm)

    # asyncpg.create_pool(...) returns an ACM whose __aenter__ yields the pool
    pool_acm = MagicMock()
    pool_acm.__aenter__ = AsyncMock(return_value=mock_pool)
    pool_acm.__aexit__ = AsyncMock(return_value=False)

    return pool_acm, mock_pool, mock_conn


async def test_all_checks_succeed_returns_zero(tmp_path):
    for name in ("check_a", "check_b"):
        d = tmp_path / name
        d.mkdir()
        (d / "01.sql").write_text("SELECT 1")

    checks = {"check_a": {}, "check_b": {}}
    pool_acm, mock_pool, _ = _make_pool(fetch_return=[{"x": 1}])

    with patch("check_runner.has_recent_locations", return_value=True), \
         patch("check_runner.asyncpg.create_pool", return_value=pool_acm), \
         patch("check_runner.CHECKS", checks):
        exit_code = await run_once_async(tmp_path, "postgresql://u:p@localhost/db")

    assert exit_code == 0


async def test_one_check_fails_returns_one(tmp_path):
    d = tmp_path / "bad_check"
    d.mkdir()
    # %(missing)s has no matching param → KeyError in convert_sql_params
    (d / "01.sql").write_text("SELECT %(missing)s")

    pool_acm, _, _ = _make_pool()
    with patch("check_runner.has_recent_locations", return_value=True), \
         patch("check_runner.asyncpg.create_pool", return_value=pool_acm), \
         patch("check_runner.CHECKS", {"bad_check": {}}):
        exit_code = await run_once_async(tmp_path, "postgresql://u:p@localhost/db")

    assert exit_code == 1


async def test_empty_checks_returns_zero(tmp_path):
    pool_acm, _, _ = _make_pool()
    with patch("check_runner.has_recent_locations", return_value=True), \
         patch("check_runner.asyncpg.create_pool", return_value=pool_acm), \
         patch("check_runner.CHECKS", {}):
        exit_code = await run_once_async(tmp_path, "postgresql://u:p@localhost/db")

    assert exit_code == 0


async def test_multiple_checks_run_concurrently(tmp_path):
    """All checks are submitted as tasks and all results processed."""
    names = ["check_1", "check_2", "check_3"]
    for name in names:
        d = tmp_path / name
        d.mkdir()
        (d / "01.sql").write_text("SELECT 1")

    checks = {n: {} for n in names}
    pool_acm, mock_pool, _ = _make_pool(fetch_return=[{"r": 1}])

    with patch("check_runner.has_recent_locations", return_value=True), \
         patch("check_runner.asyncpg.create_pool", return_value=pool_acm), \
         patch("check_runner.CHECKS", checks):
        exit_code = await run_once_async(tmp_path, "postgresql://u:p@localhost/db")

    assert exit_code == 0
    # acquire should have been called once per check
    assert mock_pool.acquire.call_count == len(names)
