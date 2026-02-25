"""Tests for run_all_checks function."""

from concurrent.futures import ThreadPoolExecutor
from unittest.mock import MagicMock

from check_runner import run_all_checks


def test_run_all_checks_all_scripts_succeed():
    pool = MagicMock()
    executor = ThreadPoolExecutor(max_workers=2)

    scripts = [
        ("check1", [("01_stage.sql", "SELECT 1")]),
        ("check2", [("01_stage.sql", "SELECT 2")]),
    ]
    contexts = {}

    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.description = ["col"]
    mock_cursor.fetchall.return_value = [(1,)]
    mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
    mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=False)
    pool.getconn.return_value = mock_conn

    failed = run_all_checks(executor, pool, scripts, contexts)

    assert failed == 0
    assert pool.getconn.call_count == 2
    assert pool.putconn.call_count == 2


def test_run_all_checks_some_scripts_fail():
    pool = MagicMock()
    executor = ThreadPoolExecutor(max_workers=2)

    scripts = [
        ("check1", [("01_stage.sql", "SELECT 1")]),
        ("check2", [("01_stage.sql", "SELECT 2")]),
    ]
    contexts = {}

    call_count = [0]

    def mock_getconn():
        conn = MagicMock()
        cursor = MagicMock()
        call_count[0] += 1
        if call_count[0] == 1:
            cursor.description = ["col"]
            cursor.fetchall.return_value = [(1,)]
        else:
            cursor.execute.side_effect = Exception("SQL error")
        conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
        conn.cursor.return_value.__exit__ = MagicMock(return_value=False)
        return conn

    pool.getconn.side_effect = mock_getconn

    failed = run_all_checks(executor, pool, scripts, contexts)

    assert failed == 1


def test_run_all_checks_with_contexts():
    pool = MagicMock()
    executor = ThreadPoolExecutor(max_workers=1)

    scripts = [
        ("check1", [("01_stage.sql", "SELECT * FROM test WHERE id = %(id)s")]),
    ]
    contexts = {"check1": {"id": 123}}

    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.description = ["col"]
    mock_cursor.fetchall.return_value = [(1,)]
    mock_conn.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
    mock_conn.cursor.return_value.__exit__ = MagicMock(return_value=False)
    pool.getconn.return_value = mock_conn

    failed = run_all_checks(executor, pool, scripts, contexts)

    assert failed == 0
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM test WHERE id = %(id)s", {"id": 123}
    )


def test_run_all_checks_empty_scripts_list():
    pool = MagicMock()
    executor = ThreadPoolExecutor(max_workers=1)

    scripts = []
    contexts = {}

    failed = run_all_checks(executor, pool, scripts, contexts)

    assert failed == 0
    pool.getconn.assert_not_called()
