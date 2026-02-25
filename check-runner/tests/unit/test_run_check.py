"""Tests for run_check function."""

from unittest.mock import MagicMock

import pytest

from check_runner import run_check


def test_run_check_successful():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = ["col1"]
    cursor.fetchall.return_value = [(1,), (2,), (3,)]
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    result = run_check(conn, "test.sql", "SELECT * FROM test", {})

    assert result == {"script": "test.sql", "status": "ok", "rows": 3}
    cursor.execute.assert_called_once_with("SELECT * FROM test", {})


def test_run_check_with_parameters():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = ["col1"]
    cursor.fetchall.return_value = [(1,)]
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    context = {"device_id": "123", "hours": 24}
    result = run_check(conn, "test.sql", "SELECT * FROM devices WHERE id = %(device_id)s", context)

    assert result == {"script": "test.sql", "status": "ok", "rows": 1}
    cursor.execute.assert_called_once_with(
        "SELECT * FROM devices WHERE id = %(device_id)s", context
    )


def test_run_check_missing_parameter():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.execute.side_effect = KeyError("device_id")
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    with pytest.raises(ValueError, match="Missing parameter: 'device_id'"):
        run_check(conn, "test.sql", "SELECT * FROM devices WHERE id = %(device_id)s", {})


def test_run_check_no_results():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = None
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    result = run_check(conn, "test.sql", "INSERT INTO test VALUES (1)", {})

    assert result == {"script": "test.sql", "status": "ok", "rows": 0}


def test_run_check_empty_results():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = ["col1"]
    cursor.fetchall.return_value = []
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    result = run_check(conn, "test.sql", "SELECT * FROM test WHERE 1=0", {})

    assert result == {"script": "test.sql", "status": "ok", "rows": 0}
