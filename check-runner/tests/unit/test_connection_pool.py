"""Tests for asyncpg connection pool setup in run_once_async."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from check_runner import run_once_async


def _make_pool_acm(fetch_return=None):
    """Build a full mock chain: pool_acm (returned by create_pool) → pool → conn.

    asyncpg.create_pool(...) is used as 'async with asyncpg.create_pool(...) as pool'.
    pool.acquire() and conn.transaction() are sync calls returning async CMs.
    """
    mock_conn = AsyncMock()
    mock_conn.fetch.return_value = fetch_return if fetch_return is not None else []
    mock_conn.execute.return_value = "SELECT 0"

    mock_transaction_cm = MagicMock()
    mock_transaction_cm.__aenter__ = AsyncMock(return_value=None)
    mock_transaction_cm.__aexit__ = AsyncMock(return_value=False)
    mock_conn.transaction = MagicMock(return_value=mock_transaction_cm)

    mock_acquire_cm = MagicMock()
    mock_acquire_cm.__aenter__ = AsyncMock(return_value=mock_conn)
    mock_acquire_cm.__aexit__ = AsyncMock(return_value=False)

    mock_pool = MagicMock()
    mock_pool.acquire = MagicMock(return_value=mock_acquire_cm)

    pool_acm = MagicMock()
    pool_acm.__aenter__ = AsyncMock(return_value=mock_pool)
    pool_acm.__aexit__ = AsyncMock(return_value=False)

    return pool_acm, mock_pool


async def test_run_once_async_creates_pool_with_correct_params(tmp_path):
    """run_once_async calls asyncpg.create_pool with min_size=1, max_size=20."""
    check_dir = tmp_path / "my_check"
    check_dir.mkdir()
    (check_dir / "01_stage.sql").write_text("SELECT 1")

    pool_acm, _ = _make_pool_acm()

    with patch("check_runner.has_recent_locations", return_value=True), \
         patch("check_runner.asyncpg.create_pool", return_value=pool_acm) as mock_create, \
         patch("check_runner.CHECKS", {"my_check": {"script_folder": "my_check"}}):
        exit_code = await run_once_async(tmp_path, "postgresql://user:pass@localhost/db")

    mock_create.assert_called_once_with(
        dsn="postgresql://user:pass@localhost/db", min_size=1, max_size=20
    )
    assert exit_code == 0


async def test_run_once_async_pool_cleanup_on_check_exception(tmp_path):
    """Pool __aexit__ is called even when a check raises an exception."""
    check_dir = tmp_path / "bad_check"
    check_dir.mkdir()
    (check_dir / "01.sql").write_text("SELECT %(missing_param)s")

    pool_acm, _ = _make_pool_acm()

    with patch("check_runner.has_recent_locations", return_value=True), \
         patch("check_runner.asyncpg.create_pool", return_value=pool_acm), \
         patch("check_runner.CHECKS", {"bad_check": {}}):
        exit_code = await run_once_async(tmp_path, "postgresql://user:pass@localhost/db")

    pool_acm.__aexit__.assert_called_once()
    assert exit_code == 1


async def test_run_once_async_skips_pool_when_no_recent_data(tmp_path):
    """Pool is never created if has_recent_locations returns False."""
    with patch("check_runner.has_recent_locations", return_value=False), \
         patch("check_runner.asyncpg.create_pool") as mock_create:
        exit_code = await run_once_async(tmp_path, "postgresql://user:pass@localhost/db")

    mock_create.assert_not_called()
    assert exit_code == 0
