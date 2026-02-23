import csv
import pathlib
import contextlib
import dataclasses
from typing import Iterable

from geotab_downloader.client import create_geotab_client


@dataclasses.dataclass(frozen=True)
class GeoTabEntity:
    csv_output_name: str
    expected_input_fields: Iterable[str]
    output_fields: Iterable[str]

    @classmethod
    def validate_fields(cls, rows: list[dict]) -> None:
        for row in rows:
            for field in cls.expected_input_fields:
                if field not in row:
                    raise ValueError(
                        f"Expected field '{field}' missing from {cls.__name__} row"
                    )

    @classmethod
    @contextlib.contextmanager
    def open_csv_for_write(
        cls, base_dir: pathlib.PurePath, write_header: bool = True
    ) -> Iterable[csv.DictWriter]:
        path = base_dir / cls.csv_output_name
        with open(path, "w", newline="") as buffer:
            writer = csv.DictWriter(
                buffer, fieldnames=cls.output_fields, extrasaction="ignore"
            )
            if write_header:
                writer.writeheader()
            yield writer


@dataclasses.dataclass(frozen=True)
class Device(GeoTabEntity):
    csv_output_name: str = "device.csv"
    expected_input_fields: Iterable[str] = ("id", "name", "deviceType")
    output_fields: Iterable[str] = ("id", "name", "deviceType")


@dataclasses.dataclass(frozen=True)
class LogRecord(GeoTabEntity):
    csv_output_name: str = "logrecord.csv"
    expected_input_fields: Iterable[str] = (
        "id",
        "dateTime",
        "speed",
        "latitude",
        "longitude",
    )
    output_fields: Iterable[str] = (
        "device_id",
        "id",
        "dateTime",
        "speed",
        "latitude",
        "longitude",
    )


@dataclasses.dataclass(frozen=True)
class StatusData(GeoTabEntity):
    csv_output_name: str = "statusdata.csv"
    expected_input_fields: Iterable[str] = ("id", "dateTime", "data", "diagnostic")
    output_fields: Iterable[str] = (
        "device_id",
        "diagnostic_id",
        "id",
        "dateTime",
        "data",
    )


@dataclasses.dataclass(frozen=True)
class Trip(GeoTabEntity):
    csv_output_name: str = "trip.csv"
    expected_input_fields: Iterable[str] = ("id", "start", "stop", "distance")
    output_fields: Iterable[str] = (
        "device_id",
        "id",
        "start",
        "stop",
        "distance",
        "drivingDuration",
        "stopDuration",
    )


@dataclasses.dataclass(frozen=True)
class Diagnostic(GeoTabEntity):
    csv_output_name: str = "diagnostic.csv"
    expected_input_fields: Iterable[str] = ("id", "name", "diagnosticType", "source")
    output_fields: Iterable[str] = (
        "id",
        "name",
        "diagnosticType",
        "source",
        "unitOfMeasure",
    )


def fetch_diagnostics_by_ids(api, diagnostic_ids: set[str]) -> list[dict]:
    diagnostics = []
    for diag_id in diagnostic_ids:
        response = api.get("Diagnostic", id=diag_id)
        if not isinstance(response, list) or len(response) != 1:
            raise ValueError(
                f"Expected exactly 1 diagnostic with id {diag_id}, got {response}"
            )
        diagnostics.append(response[0])
    return diagnostics


def download_all(
    api, *, output_dir: pathlib.Path = pathlib.Path("geotab_db_data")
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    devices = api.get("Device")
    Device.validate_fields(devices)
    with Device.open_csv_for_write(output_dir) as writer:
        writer.writerows(devices)

    utilized_diagnostics = set()

    with contextlib.ExitStack() as stack:
        trips_writer = stack.enter_context(Trip.open_csv_for_write(output_dir))
        statuses_writer = stack.enter_context(StatusData.open_csv_for_write(output_dir))
        log_records_writer = stack.enter_context(
            LogRecord.open_csv_for_write(output_dir)
        )

        for device in devices:
            device_id = device["id"]
            geotab_query = {"deviceSearch": {"id": device_id}}

            statuses = api.get("StatusData", search=geotab_query)
            StatusData.validate_fields(statuses)
            for status in statuses:
                status["device_id"] = device_id
                status["diagnostic_id"] = status["diagnostic"]["id"]
                utilized_diagnostics.add(status["diagnostic"]["id"])
            statuses_writer.writerows(statuses)

            log_records = api.get("LogRecord", search=geotab_query)
            LogRecord.validate_fields(log_records)
            for record in log_records:
                record["device_id"] = device_id
            log_records_writer.writerows(log_records)

            trips = api.get("Trip", search=geotab_query)
            Trip.validate_fields(trips)
            for trip in trips:
                trip["device_id"] = device_id
            trips_writer.writerows(trips)

    if utilized_diagnostics:
        diagnostics = fetch_diagnostics_by_ids(api, utilized_diagnostics)
        Diagnostic.validate_fields(diagnostics)
        with Diagnostic.open_csv_for_write(output_dir) as writer:
            writer.writerows(diagnostics)
