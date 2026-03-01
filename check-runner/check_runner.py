"""Check-runner service. Periodically runs SQL scripts from scripts folder."""

import json
import logging
import os
import sys
from collections.abc import Callable, Mapping
from concurrent.futures import Executor, ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from psycopg2 import pool as psycopg2_pool
import psycopg2
from psycopg2.extensions import connection as PgConnection
from psycopg2.extras import Json

logger = logging.getLogger("check-runner")

# Type alias: (check_name, stages, params) where stages is list of (stage_name, sql)
CheckScript = tuple[str, list[tuple[str, str]], Mapping[str, Any]]

# Check configurations: maps check name to its configuration
# Each check has:
#   - script_folder: directory under scripts/ containing SQL files
#   - params: dict of parameters passed to SQL via %(name)s syntax

CHECKS: Mapping[str, Mapping[str, Any]] = {
    # Fuel Consumption Anomaly
    # Detects fuel efficiency loss (tire pressure issues, engine degradation, fuel leaks, driver behavior changes)
    # Diagnostic: Trip fuel used (DiagnosticTotalTripFuelUsedId)
    # Unit: Liters
    "road-counter-fuel-consumption": {
        "script_folder": "road-counter",
        "params": {
            "target_interval_end": "$NOW",
            "target_interval_depth_minutes": timedelta(hours=4),
            "historical_interval_end": "$NOW",
            "historical_interval_depth_minutes": timedelta(hours=12),
            "diagnostic_ids": ["DiagnosticTotalTripFuelUsedId"],
            "warning_threshold": 0.6,
            "error_threshold": 0.8,
            "segment_proximity_filter": 0.005,
            "validation_type": "ROAD_COUNTER_FUEL_CONSUMPTION",
            "done": "DONE",
        },
    },
    # Coolant Temperature Rising
    # Early warning of cooling system issues (coolant leaks, radiator blockage, thermostat failure)
    # Diagnostic: Engine coolant temperature (DiagnosticEngineCoolantTemperatureId)
    # Unit: Degrees Celsius (°C)
    "road-counter-coolant-temp": {
        "script_folder": "road-counter",
        "params": {
            "target_interval_end": "$NOW",
            "target_interval_depth_minutes": timedelta(hours=2),
            "historical_interval_end": "$NOW",
            "historical_interval_depth_minutes": timedelta(hours=12),
            "diagnostic_ids": ["DiagnosticEngineCoolantTemperatureId"],
            "warning_threshold": 0.5,
            "error_threshold": 0.65,
            "segment_proximity_filter": 0.005,
            "validation_type": "ROAD_COUNTER_COOLANT_TEMP",
            "done": "DONE",
        },
    },
    # EV Battery Discharge Rate Anomaly
    # Monitors electric vehicle battery health (degradation, parasitic loads, HVAC overuse)
    # Diagnostic: Electric vehicle battery total energy out while driving (DiagnosticElectricEnergyOutId)
    # Unit: Kilowatt-hours (kWh)
    "road-counter-ev-battery-discharge": {
        "script_folder": "road-counter",
        "params": {
            "target_interval_end": "$NOW",
            "target_interval_depth_minutes": timedelta(hours=4),
            "historical_interval_end": "$NOW",
            "historical_interval_depth_minutes": timedelta(hours=12),
            "diagnostic_ids": ["DiagnosticElectricEnergyOutId"],
            "warning_threshold": 0.05,
            "error_threshold": 0.1,
            "segment_proximity_filter": 0.005,
            "validation_type": "ROAD_COUNTER_EV_BATTERY_DISCHARGE",
            "done": "DONE",
        },
    },
}


def get_database_url(environ: Mapping[str, str]) -> str:
    database_url = environ.get("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is required")

    parsed = urlparse(database_url)
    if parsed.scheme not in ("postgresql", "postgres"):
        raise ValueError(
            f"DATABASE_URL must be a valid PostgreSQL URL "
            f"(got scheme: '{parsed.scheme or 'empty'}')"
        )
    if not parsed.hostname:
        raise ValueError("DATABASE_URL must include a host")
    if not parsed.path or parsed.path == "/":
        raise ValueError("DATABASE_URL must include a database name")

    return database_url


def run_check(
    conn: PgConnection,
    check_name: str,
    stages: list[tuple[str, str]],
    params: Mapping[str, Any],
) -> dict[str, Any]:
    """Run a multi-stage SQL check. All stages execute in one transaction."""
    total_rows = 0

    with conn.cursor() as cur:
        for stage_name, sql in stages:
            try:
                cur.execute(sql, params)
            except KeyError as e:
                param = str(e).strip("'")
                raise ValueError(f"Missing parameter: '{param}'") from None

            if cur.description:
                total_rows += len(cur.fetchall())
            else:
                total_rows += cur.rowcount

    conn.commit()
    return {
        "check": check_name,
        "status": "ok",
        "rows": total_rows,
        "stages": len(stages),
    }


@contextmanager
def db_connection_pool(dsn: str, minconn: int = 1, maxconn: int = 20) -> Any:
    pool = psycopg2_pool.ThreadedConnectionPool(
        minconn=minconn, maxconn=maxconn, dsn=dsn
    )
    try:
        yield pool
    finally:
        pool.closeall()


def run_all_checks(
    executor: Executor,
    pool: Any,
    scripts: list[CheckScript],
) -> int:
    """Run all check scripts. Returns number of failed checks."""
    logger.info(f"Running {len(scripts)} check(s)")

    def _run_single(
        name: str, stages: list[tuple[str, str]], params: Mapping[str, Any]
    ) -> dict[str, Any]:
        conn = None
        try:
            conn = pool.getconn()
            return run_check(conn, name, stages, params)
        except Exception as e:
            logger.error(f"{name} failed: {e}")
            return {"check": name, "status": "failed", "error": str(e)}
        finally:
            if conn is not None:
                pool.putconn(conn)

    futures = [
        executor.submit(_run_single, name, stages, params)
        for name, stages, params in scripts
    ]

    failed = 0
    for future in as_completed(futures):
        result = future.result()
        if result["status"] == "failed":
            failed += 1
            logger.error(f"FAILED: {result['check']} - {result.get('error')}")
        else:
            logger.info(
                f"OK: {result['check']} ({result['rows']} rows, {result['stages']} stage(s))"
            )

    return failed


def load_scripts(
    scripts_dir: Path, checks: Mapping[str, Mapping[str, Any]]
) -> list[tuple[str, list[tuple[str, str]], Mapping[str, Any]]]:
    """Load SQL scripts from directories specified in checks.

    Each check has a 'script_folder' key pointing to the directory containing SQL files.
    SQL files within a directory are executed as stages, sorted by filename.

    Returns list of (check_name, stages, params) tuples where params are passed to SQL.

    Raises:
        FileNotFoundError: If a check directory mentioned in checks doesn't exist.
    """
    scripts: list[tuple[str, list[tuple[str, str]], Mapping[str, Any]]] = []

    for check_name, check_config in checks.items():
        folder_name = check_config.get("script_folder", check_name)
        check_dir = scripts_dir / folder_name
        if not check_dir.is_dir():
            raise FileNotFoundError(f"Check directory not found: {check_dir}")

        sql_files = sorted(check_dir.glob("*.sql"))
        if not sql_files:
            raise FileNotFoundError(
                f"No SQL files found in check directory: {check_dir}"
            )

        stages = [(f.name, f.read_text()) for f in sql_files]
        params = check_config.get("params", {})
        scripts.append((check_name, stages, params))

    return scripts


def has_recent_locations(db_url: str, window_minutes: int = 15) -> bool:
    """Return True if geotab_location has any rows within the last *window_minutes*.

    Used as a lightweight pre-flight guard so checks are skipped when the
    backend has been down long enough that no new data has arrived yet.
    """
    from_dt = datetime.now(tz=timezone.utc) - timedelta(minutes=window_minutes)
    conn = psycopg2.connect(db_url)
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT 1 FROM geotab_location WHERE datetime >= %s LIMIT 1",
                (from_dt,),
            )
            return cur.fetchone() is not None
    finally:
        conn.close()


def _resolve_param_markers(params: Mapping[str, Any]) -> dict[str, Any]:
    """Replace parameter markers like '$NOW' with actual values."""
    resolved = {}
    for key, val in params.items():
        if val == "$NOW":
            resolved[key] = datetime.now(tz=timezone.utc).replace(
                second=0, microsecond=0
            )
        else:
            resolved[key] = val
    return resolved


def run_once(
    scripts_dir: Path,
    db_url: str,
    max_workers: int,
    executor_factory: Callable[..., Executor],
    pool_factory: Callable[..., Any],
) -> int:
    """Run all checks once. Returns exit code."""
    if not has_recent_locations(db_url):
        logger.info("Skipping checks: no geotab_location data in the last 15 minutes")
        return 0

    try:
        scripts = load_scripts(scripts_dir, CHECKS)
    except FileNotFoundError as e:
        logger.error(f"Failed to load scripts: {e}")
        return 1

    # Resolve parameter markers (e.g., '$NOW') for each check
    resolved_scripts = [
        (name, stages, _resolve_param_markers(params))
        for name, stages, params in scripts
    ]

    with executor_factory(max_workers=max_workers) as executor:
        with pool_factory(dsn=db_url, minconn=1, maxconn=max_workers) as pool:
            failed = run_all_checks(executor, pool, resolved_scripts)

    if failed:
        logger.error(f"{failed} check(s) failed")
        return 1

    logger.info("All checks completed successfully")
    return 0


def main(
    scripts_dir: Path = Path("./scripts"),
    environ: Mapping[str, str] | None = None,
    max_workers: int = 20,
    executor_factory: Callable[..., Executor] | None = None,
    pool_factory: Callable[..., Any] | None = None,
) -> int:
    """Entry point. Returns exit code (0 for success, 1 for failure).

    Set CHECK_INTERVAL_SECONDS env var to run in a loop.
    """
    import time

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    if environ is None:
        environ = os.environ
    if executor_factory is None:
        executor_factory = ThreadPoolExecutor
    if pool_factory is None:
        pool_factory = db_connection_pool

    try:
        db_url = get_database_url(environ)
    except ValueError as e:
        logger.error(f"Invalid DATABASE_URL: {e}")
        return 1

    interval_str = environ.get("CHECK_INTERVAL_SECONDS", "900")  # Default to 15 minutes
    if interval_str is None:
        return run_once(
            scripts_dir, db_url, max_workers, executor_factory, pool_factory
        )

    interval_seconds = int(interval_str)
    logger.info(f"Starting scheduler: running checks every {interval_seconds}s")
    while True:
        exit_code = run_once(
            scripts_dir, db_url, max_workers, executor_factory, pool_factory
        )
        if exit_code != 0:
            logger.warning(f"Check run failed, will retry in {interval_seconds}s")
        time.sleep(interval_seconds)


if __name__ == "__main__":
    sys.exit(main())
