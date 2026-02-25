"""Tests for get_database_url function."""

import pytest

from check_runner import get_database_url


def test_get_database_url_valid_postgresql():
    environ = {"DATABASE_URL": "postgresql://user:pass@localhost:5432/dbname"}
    result = get_database_url(environ)
    assert result == "postgresql://user:pass@localhost:5432/dbname"


def test_get_database_url_valid_postgres():
    environ = {"DATABASE_URL": "postgres://user:pass@localhost:5432/dbname"}
    result = get_database_url(environ)
    assert result == "postgres://user:pass@localhost:5432/dbname"


def test_get_database_url_missing():
    environ = {}
    with pytest.raises(ValueError, match="DATABASE_URL environment variable is required"):
        get_database_url(environ)


def test_get_database_url_empty():
    environ = {"DATABASE_URL": ""}
    with pytest.raises(ValueError, match="DATABASE_URL environment variable is required"):
        get_database_url(environ)


def test_get_database_url_invalid_scheme():
    environ = {"DATABASE_URL": "mysql://user:pass@localhost:5432/dbname"}
    with pytest.raises(ValueError, match="must be a valid PostgreSQL URL"):
        get_database_url(environ)


def test_get_database_url_missing_scheme():
    environ = {"DATABASE_URL": "user:pass@localhost/dbname"}
    with pytest.raises(ValueError, match="must be a valid PostgreSQL URL"):
        get_database_url(environ)


def test_get_database_url_missing_host():
    environ = {"DATABASE_URL": "postgresql:///dbname"}
    with pytest.raises(ValueError, match="must include a host"):
        get_database_url(environ)


def test_get_database_url_missing_database_name():
    environ = {"DATABASE_URL": "postgresql://user:pass@localhost:5432/"}
    with pytest.raises(ValueError, match="must include a database name"):
        get_database_url(environ)
