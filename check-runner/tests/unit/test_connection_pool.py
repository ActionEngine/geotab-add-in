"""Tests for db_connection_pool context manager."""

from unittest.mock import MagicMock, patch

import pytest

from check_runner import db_connection_pool


@patch("check_runner.psycopg2_pool.ThreadedConnectionPool")
def test_connection_pool_context_manager_creates_pool(mock_pool_class):
    mock_pool = MagicMock()
    mock_pool_class.return_value = mock_pool

    with db_connection_pool(dsn="postgresql://user:pass@localhost/db") as pool:
        pool.getconn()

    mock_pool_class.assert_called_once_with(
        minconn=1, maxconn=20, dsn="postgresql://user:pass@localhost/db"
    )
    mock_pool.closeall.assert_called_once()


@patch("check_runner.psycopg2_pool.ThreadedConnectionPool")
def test_connection_pool_context_manager_with_exception(mock_pool_class):
    mock_pool = MagicMock()
    mock_pool_class.return_value = mock_pool

    with pytest.raises(ValueError):
        with db_connection_pool(dsn="postgresql://user:pass@localhost/db") as pool:
            raise ValueError("Test error")

    mock_pool.closeall.assert_called_once()


@patch("check_runner.psycopg2_pool.ThreadedConnectionPool")
def test_connection_pool_custom_minconn_maxconn(mock_pool_class):
    mock_pool = MagicMock()
    mock_pool_class.return_value = mock_pool

    with db_connection_pool(dsn="postgresql://user:pass@localhost/db", minconn=2, maxconn=10) as pool:
        pass

    mock_pool_class.assert_called_once_with(minconn=2, maxconn=10, dsn="postgresql://user:pass@localhost/db")
