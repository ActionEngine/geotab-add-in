import csv
from unittest.mock import MagicMock

import pytest

from geotab_downloader.download import (
    GeoTabEntity,
    download_all,
    fetch_diagnostics_by_ids,
)


def test_geotab_entity_validate_fields_success():
    rows = [
        {"id": "1", "name": "test"},
        {"id": "2", "name": "test2"},
    ]

    class TestEntity(GeoTabEntity):
        csv_output_name = "test.csv"
        expected_input_fields = ("id", "name")
        output_fields = ("id", "name")

    TestEntity.validate_fields(rows)


def test_geotab_entity_validate_fields_missing_field():
    rows = [
        {"id": "1", "name": "test"},
        {"id": "2"},
    ]

    class TestEntity(GeoTabEntity):
        csv_output_name = "test.csv"
        expected_input_fields = ("id", "name")
        output_fields = ("id", "name")

    with pytest.raises(ValueError, match="Expected field 'name' missing"):
        TestEntity.validate_fields(rows)


def test_geotab_entity_open_csv_for_write_creates_file(tmp_path):
    class TestEntity(GeoTabEntity):
        csv_output_name = "test.csv"
        expected_input_fields = ("id", "name")
        output_fields = ("id", "name")

    with TestEntity.open_csv_for_write(tmp_path) as writer:
        writer.writerow({"id": "1", "name": "test"})

    output_file = tmp_path / "test.csv"
    assert output_file.exists()

    with open(output_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["id"] == "1"
        assert rows[0]["name"] == "test"


def test_geotab_entity_open_csv_for_write_without_header(tmp_path):
    class TestEntity(GeoTabEntity):
        csv_output_name = "test.csv"
        expected_input_fields = ("id", "name")
        output_fields = ("id", "name")

    with TestEntity.open_csv_for_write(tmp_path, write_header=False) as writer:
        writer.writerow({"id": "1", "name": "test"})

    output_file = tmp_path / "test.csv"
    with open(output_file) as f:
        content = f.read()
        assert not content.startswith("id,name")
        assert "1,test" in content


def test_fetch_diagnostics_by_ids_single_diagnostic():
    mock_api = MagicMock()
    mock_api.get.return_value = [
        {
            "id": "diag1",
            "name": "Diagnostic 1",
            "diagnosticType": "Type1",
            "source": "Source1",
        }
    ]

    result = fetch_diagnostics_by_ids(mock_api, {"diag1"})

    assert len(result) == 1
    assert result[0]["id"] == "diag1"
    mock_api.get.assert_called_once_with("Diagnostic", id="diag1")


def test_fetch_diagnostics_by_ids_multiple_diagnostics():
    mock_api = MagicMock()
    diagnostics_data = {
        "diag1": {
            "id": "diag1",
            "name": "Diagnostic 1",
            "diagnosticType": "Type1",
            "source": "Source1",
        },
        "diag2": {
            "id": "diag2",
            "name": "Diagnostic 2",
            "diagnosticType": "Type2",
            "source": "Source2",
        },
    }
    mock_api.get.side_effect = lambda entity_type, id: [diagnostics_data[id]]

    result = fetch_diagnostics_by_ids(mock_api, {"diag1", "diag2"})

    assert len(result) == 2
    assert {d["id"] for d in result} == {"diag1", "diag2"}


def test_fetch_diagnostics_by_ids_raises_on_invalid_response():
    mock_api = MagicMock()
    mock_api.get.return_value = []

    with pytest.raises(ValueError, match="Expected exactly 1 diagnostic"):
        fetch_diagnostics_by_ids(mock_api, {"diag1"})


def test_download_all_creates_output_directory(tmp_path):
    output_dir = tmp_path / "output"
    mock_api = MagicMock()
    mock_api.get.side_effect = lambda entity_type, **kwargs: []

    download_all(mock_api, output_dir=output_dir)

    assert output_dir.exists()
    assert output_dir.is_dir()


def test_download_all_downloads_devices(tmp_path):
    mock_api = MagicMock()
    devices = [{"id": "dev1", "name": "Device 1", "deviceType": "Type1"}]
    mock_api.get.side_effect = lambda entity_type, **kwargs: {
        "Device": devices,
        "StatusData": [],
        "LogRecord": [],
        "Trip": [],
    }.get(entity_type, [])

    download_all(mock_api, output_dir=tmp_path)

    device_file = tmp_path / "device.csv"
    assert device_file.exists()

    with open(device_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["id"] == "dev1"


def test_download_all_downloads_log_records(tmp_path):
    mock_api = MagicMock()
    devices = [{"id": "dev1", "name": "Device 1", "deviceType": "Type1"}]
    log_records = [
        {
            "id": "log1",
            "dateTime": "2026-01-01",
            "speed": "60",
            "latitude": "40.7",
            "longitude": "-74.0",
        }
    ]

    def mock_get(entity_type, **kwargs):
        if entity_type == "Device":
            return devices
        elif entity_type == "LogRecord":
            return log_records
        return []

    mock_api.get.side_effect = mock_get

    download_all(mock_api, output_dir=tmp_path)

    logrecord_file = tmp_path / "logrecord.csv"
    assert logrecord_file.exists()

    with open(logrecord_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["id"] == "log1"
        assert rows[0]["device_id"] == "dev1"


def test_download_all_downloads_status_data(tmp_path):
    mock_api = MagicMock()
    devices = [{"id": "dev1", "name": "Device 1", "deviceType": "Type1"}]
    status_data = [
        {
            "id": "status1",
            "dateTime": "2026-01-01",
            "data": "100",
            "diagnostic": {"id": "diag1"},
        }
    ]
    diagnostics = [
        {
            "id": "diag1",
            "name": "Diagnostic 1",
            "diagnosticType": "Type1",
            "source": "Source1",
        }
    ]

    def mock_get(entity_type, **kwargs):
        if entity_type == "Device":
            return devices
        elif entity_type == "StatusData":
            return status_data
        elif entity_type == "Diagnostic":
            return diagnostics
        return []

    mock_api.get.side_effect = mock_get

    download_all(mock_api, output_dir=tmp_path)

    statusdata_file = tmp_path / "statusdata.csv"
    assert statusdata_file.exists()

    with open(statusdata_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["id"] == "status1"
        assert rows[0]["device_id"] == "dev1"
        assert rows[0]["diagnostic_id"] == "diag1"


def test_download_all_downloads_trips(tmp_path):
    mock_api = MagicMock()
    devices = [{"id": "dev1", "name": "Device 1", "deviceType": "Type1"}]
    trips = [
        {
            "id": "trip1",
            "start": "2026-01-01T08:00:00",
            "stop": "2026-01-01T09:00:00",
            "distance": "10000",
        }
    ]

    def mock_get(entity_type, **kwargs):
        if entity_type == "Device":
            return devices
        elif entity_type == "Trip":
            return trips
        return []

    mock_api.get.side_effect = mock_get

    download_all(mock_api, output_dir=tmp_path)

    trip_file = tmp_path / "trip.csv"
    assert trip_file.exists()

    with open(trip_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["id"] == "trip1"
        assert rows[0]["device_id"] == "dev1"


def test_download_all_downloads_diagnostics(tmp_path):
    mock_api = MagicMock()
    devices = [{"id": "dev1", "name": "Device 1", "deviceType": "Type1"}]
    status_data = [
        {
            "id": "status1",
            "dateTime": "2026-01-01",
            "data": "100",
            "diagnostic": {"id": "diag1"},
        }
    ]
    diagnostics = [
        {
            "id": "diag1",
            "name": "Diagnostic 1",
            "diagnosticType": "Type1",
            "source": "Source1",
        }
    ]

    def mock_get(entity_type, **kwargs):
        if entity_type == "Device":
            return devices
        elif entity_type == "StatusData":
            return status_data
        elif entity_type == "Diagnostic":
            return diagnostics
        return []

    mock_api.get.side_effect = mock_get

    download_all(mock_api, output_dir=tmp_path)

    diagnostic_file = tmp_path / "diagnostic.csv"
    assert diagnostic_file.exists()

    with open(diagnostic_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["id"] == "diag1"


def test_download_all_no_diagnostics_when_no_status_data(tmp_path):
    mock_api = MagicMock()
    devices = [{"id": "dev1", "name": "Device 1", "deviceType": "Type1"}]
    mock_api.get.side_effect = lambda entity_type, **kwargs: (
        devices if entity_type == "Device" else []
    )

    download_all(mock_api, output_dir=tmp_path)

    diagnostic_file = tmp_path / "diagnostic.csv"
    assert not diagnostic_file.exists()


def test_download_all_with_multiple_devices(tmp_path):
    mock_api = MagicMock()
    devices = [
        {"id": "dev1", "name": "Device 1", "deviceType": "Type1"},
        {"id": "dev2", "name": "Device 2", "deviceType": "Type2"},
    ]
    log_records = [
        {
            "id": "log1",
            "dateTime": "2026-01-01",
            "speed": "60",
            "latitude": "40.7",
            "longitude": "-74.0",
        }
    ]

    def mock_get(entity_type, **kwargs):
        if entity_type == "Device":
            return devices
        elif entity_type == "LogRecord":
            return log_records
        return []

    mock_api.get.side_effect = mock_get

    download_all(mock_api, output_dir=tmp_path)

    logrecord_file = tmp_path / "logrecord.csv"
    with open(logrecord_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 2
        assert {row["device_id"] for row in rows} == {"dev1", "dev2"}


def test_download_all_validates_fields(tmp_path):
    mock_api = MagicMock()
    devices = [{"id": "dev1", "name": "Device 1"}]
    mock_api.get.return_value = devices

    with pytest.raises(ValueError, match="Expected field 'deviceType' missing"):
        download_all(mock_api, output_dir=tmp_path)


def test_download_all_uses_default_output_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    mock_api = MagicMock()
    devices = [{"id": "dev1", "name": "Device 1", "deviceType": "Type1"}]
    mock_api.get.side_effect = lambda entity_type, **kwargs: (
        devices if entity_type == "Device" else []
    )

    download_all(mock_api)

    default_dir = tmp_path / "geotab_db_data"
    assert default_dir.exists()
    assert (default_dir / "device.csv").exists()
