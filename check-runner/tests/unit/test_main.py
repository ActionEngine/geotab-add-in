"""Tests for main function."""

import logging
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from check_runner import main


# Script folders referenced by CHECKS (check name -> folder name)
# Both road-counter checks use the same "road-counter" script folder
REQUIRED_SCRIPT_FOLDERS = ["road-counter"]


def setup_check_dirs(tmp_path):
    """Helper to create the required check directory structures."""
    for folder_name in REQUIRED_SCRIPT_FOLDERS:
        check_dir = tmp_path / folder_name
        check_dir.mkdir()
        (check_dir / "01_stage.sql").write_text("SELECT 1")
    return tmp_path


async def test_main_missing_database_url_returns_one(tmp_path):
    """main() returns 1 when DATABASE_URL is absent."""
    setup_check_dirs(tmp_path)
    exit_code = await main(scripts_dir=tmp_path, environ={})
    assert exit_code == 1


async def test_main_invalid_database_url_returns_one(tmp_path):
    """main() returns 1 when DATABASE_URL has an invalid scheme."""
    setup_check_dirs(tmp_path)
    exit_code = await main(
        scripts_dir=tmp_path,
        environ={"DATABASE_URL": "mysql://user:pass@localhost/db"},
    )
    assert exit_code == 1


async def test_main_no_recent_data_returns_zero(tmp_path):
    """main() returns 0 (skip) when has_recent_locations is False."""
    setup_check_dirs(tmp_path)
    with patch("check_runner.has_recent_locations", return_value=False):
        exit_code = await main(
            scripts_dir=tmp_path,
            environ={"DATABASE_URL": "postgresql://u:p@localhost/db"},
        )
    assert exit_code == 0


async def test_main_checks_pass_returns_zero(tmp_path):
    """main() returns 0 when all checks succeed."""
    setup_check_dirs(tmp_path)

    mock_conn = AsyncMock()
    mock_conn.fetch.return_value = [{"x": 1}]

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

    with patch("check_runner.has_recent_locations", return_value=True), \
         patch("check_runner.asyncpg.create_pool", return_value=pool_acm):
        exit_code = await main(
            scripts_dir=tmp_path,
            environ={"DATABASE_URL": "postgresql://u:p@localhost/db"},
        )
    assert exit_code == 0


async def test_main_uses_os_environ_by_default(tmp_path, monkeypatch):
    """main() reads DATABASE_URL from os.environ when environ arg is None."""
    setup_check_dirs(tmp_path)
    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@localhost/db")
    with patch("check_runner.has_recent_locations", return_value=False):
        exit_code = await main(scripts_dir=tmp_path)
    assert exit_code == 0
