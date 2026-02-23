from unittest.mock import MagicMock, mock_open, patch

import mygeotab
import pytest

import geotab_downloader.client as client


def test_session_filename():
    result = client.session_filename("user123", "db456")
    assert result == "./geotab-session-user123@db456"


def test_is_session_saved_when_file_exists():
    with patch("os.path.exists") as mock_exists:
        mock_exists.side_effect = lambda path: path == "./geotab-session-user@database"
        result = client.is_session_saved("user", "database")
    assert result is True


def test_is_session_saved_when_file_not_exists():
    with patch("os.path.exists", return_value=False):
        result = client.is_session_saved("user", "database")
    assert result is False


def test_save_session_id():
    mock_file = mock_open()
    with patch("builtins.open", mock_file):
        client.save_session_id("user", "database", "session123")

    mock_file.assert_called_once_with("./geotab-session-user@database", "w")
    mock_file().write.assert_called_once_with("session123")


def test_load_saved_session():
    mock_file = mock_open(read_data="session456\n")
    with patch("builtins.open", mock_file):
        result = client.load_saved_session("user", "database")

    mock_file.assert_called_once_with("./geotab-session-user@database", "r")
    assert result == "session456"


def test_get_new_session_id():
    mock_api = MagicMock()
    mock_api.credentials.session_id = "new_session_123"

    with patch("mygeotab.API", return_value=mock_api):
        result = client.get_new_session_id("user", "database", "password")

    mock_api.authenticate.assert_called_once()
    assert result == "new_session_123"


def test_is_session_valid_returns_true():
    mock_api = MagicMock()
    mock_api.call.return_value = [{"name": "user"}]

    with patch("mygeotab.API", return_value=mock_api):
        result = client.is_session_valid("user", "database", "valid_session")

    mock_api.call.assert_called_once_with(
        "Get", typeName="User", search={"name": "user"}
    )
    assert result is True


def test_is_session_valid_returns_false():
    mock_api = MagicMock()
    mock_api.call.side_effect = mygeotab.AuthenticationException(
        username="user", database="database", server="my.geotab.com"
    )

    with patch("mygeotab.API", return_value=mock_api):
        result = client.is_session_valid("user", "database", "invalid_session")

    assert result is False


def test_create_geotab_client_no_saved_session():
    mock_api = MagicMock()

    with (
        patch("geotab_downloader.client.is_session_saved", return_value=False),
        patch(
            "geotab_downloader.client.get_new_session_id", return_value="new_session_id"
        ),
        patch("geotab_downloader.client.save_session_id") as mock_save,
        patch("mygeotab.API", return_value=mock_api),
    ):
        result = client.create_geotab_client("user", "database", "password")

    mock_save.assert_called_once_with("user", "database", "new_session_id")
    assert result == mock_api


def test_create_geotab_client_with_valid_saved_session():
    mock_api = MagicMock()

    with (
        patch("geotab_downloader.client.is_session_saved", return_value=True),
        patch(
            "geotab_downloader.client.load_saved_session", return_value="saved_session"
        ),
        patch("geotab_downloader.client.is_session_valid", return_value=True),
        patch("mygeotab.API", return_value=mock_api),
    ):
        result = client.create_geotab_client("user", "database", "password")

    assert result == mock_api


def test_create_geotab_client_with_invalid_saved_session():
    mock_api = MagicMock()

    with (
        patch("geotab_downloader.client.is_session_saved", return_value=True),
        patch(
            "geotab_downloader.client.load_saved_session",
            return_value="invalid_session",
        ),
        patch("geotab_downloader.client.is_session_valid", return_value=False),
        patch(
            "geotab_downloader.client.get_new_session_id", return_value="new_session"
        ),
        patch("geotab_downloader.client.save_session_id") as mock_save,
        patch("mygeotab.API", return_value=mock_api),
    ):
        result = client.create_geotab_client("user", "database", "password")

    mock_save.assert_called_once_with("user", "database", "new_session")
    assert result == mock_api
