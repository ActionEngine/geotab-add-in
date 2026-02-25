"""Tests for main function."""

import logging
from contextlib import contextmanager
from unittest.mock import MagicMock, patch

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


def test_main_no_scripts_found(tmp_path, caplog):
    """Test that main exits with error when contexts references non-existent check."""
    caplog.set_level(logging.ERROR)
    environ = {"DATABASE_URL": "postgresql://user:pass@localhost/db"}

    result = main(scripts_dir=tmp_path, environ=environ)

    assert result == 1
    assert "Failed to load scripts" in caplog.text
    assert "Check directory not found" in caplog.text


def test_main_invalid_database_url(tmp_path, caplog):
    caplog.set_level(logging.ERROR)
    setup_check_dirs(tmp_path)

    environ = {"DATABASE_URL": "invalid-url"}

    result = main(scripts_dir=tmp_path, environ=environ)

    assert result == 1
    assert "Invalid DATABASE_URL" in caplog.text


def test_main_missing_database_url(tmp_path, caplog):
    caplog.set_level(logging.ERROR)
    setup_check_dirs(tmp_path)

    environ = {}

    result = main(scripts_dir=tmp_path, environ=environ)

    assert result == 1
    assert "Invalid DATABASE_URL" in caplog.text


def test_main_successful_execution(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    setup_check_dirs(tmp_path)

    environ = {"DATABASE_URL": "postgresql://user:pass@localhost/db"}

    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.description = ["col"]
    mock_cursor.fetchall.return_value = [(1,)]
    mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
    mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    mock_pool = MagicMock()
    mock_pool.getconn.return_value = mock_conn

    @contextmanager
    def mock_pool_factory(**kwargs):
        yield mock_pool

    result = main(
        scripts_dir=tmp_path,
        environ=environ,
        max_workers=1,
        pool_factory=mock_pool_factory,
    )

    assert result == 0
    assert "All checks completed successfully" in caplog.text


@patch("check_runner.run_all_checks")
def test_main_with_failing_check(mock_run_all_checks, tmp_path, caplog):
    caplog.set_level(logging.ERROR)
    setup_check_dirs(tmp_path)

    environ = {"DATABASE_URL": "postgresql://user:pass@localhost/db"}

    mock_run_all_checks.return_value = 1
    mock_pool = MagicMock()

    @contextmanager
    def mock_pool_factory(**kwargs):
        yield mock_pool

    result = main(
        scripts_dir=tmp_path,
        environ=environ,
        max_workers=1,
        pool_factory=mock_pool_factory,
    )

    assert result == 1
    assert "1 check(s) failed" in caplog.text
