"""Tests for run_check function."""

from unittest.mock import MagicMock, call

import pytest

from check_runner import run_check


def test_run_check_single_stage():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = ["col1"]
    cursor.fetchall.return_value = [(1,), (2,), (3,)]
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    stages = [("01_select.sql", "SELECT * FROM test")]
    result = run_check(conn, "my_check", stages, {})

    assert result == {"check": "my_check", "status": "ok", "rows": 3, "stages": 1}
    cursor.execute.assert_called_once_with("SELECT * FROM test", {})


def test_run_check_multiple_stages():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = None
    cursor.rowcount = 5
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    stages = [
        ("01_cleanup.sql", "DELETE FROM old"),
        ("02_insert.sql", "INSERT INTO new VALUES (1)"),
    ]
    result = run_check(conn, "my_check", stages, {})

    assert result == {"check": "my_check", "status": "ok", "rows": 10, "stages": 2}
    assert cursor.execute.call_count == 2
    cursor.execute.assert_has_calls([
        call("DELETE FROM old", {}),
        call("INSERT INTO new VALUES (1)", {}),
    ])


def test_run_check_with_parameters():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = ["col1"]
    cursor.fetchall.return_value = [(1,)]
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    context = {"device_id": "123", "hours": 24}
    stages = [("01_query.sql", "SELECT * FROM devices WHERE id = %(device_id)s")]
    result = run_check(conn, "my_check", stages, context)

    assert result == {"check": "my_check", "status": "ok", "rows": 1, "stages": 1}
    cursor.execute.assert_called_once_with(
        "SELECT * FROM devices WHERE id = %(device_id)s", context
    )


def test_run_check_missing_parameter():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.execute.side_effect = KeyError("device_id")
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    stages = [("01_query.sql", "SELECT * FROM devices WHERE id = %(device_id)s")]

    with pytest.raises(ValueError, match="Missing parameter: 'device_id'"):
        run_check(conn, "my_check", stages, {})


def test_run_check_no_results():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = None
    cursor.rowcount = 0
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    stages = [("01_insert.sql", "INSERT INTO test VALUES (1)")]
    result = run_check(conn, "my_check", stages, {})

    assert result == {"check": "my_check", "status": "ok", "rows": 0, "stages": 1}


def test_run_check_empty_results():
    conn = MagicMock()
    cursor = MagicMock()
    cursor.description = ["col1"]
    cursor.fetchall.return_value = []
    conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
    conn.cursor.return_value.__exit__ = MagicMock(return_value=False)

    stages = [("01_select.sql", "SELECT * FROM test WHERE 1=0")]
    result = run_check(conn, "my_check", stages, {})

    assert result == {"check": "my_check", "status": "ok", "rows": 0, "stages": 1}
