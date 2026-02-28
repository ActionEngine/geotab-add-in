import asyncio
import asyncpg
import logging
import os
import re
import sys
from collections.abc import Mapping
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

logger = logging.getLogger("check-runner")

# --- Configurations ---
CHECKS: Mapping[str, Mapping[str, Any]] = {
    "road-counter-2h": {
        "script_folder": "road-counter",
        "params": {
            "target_interval_end": "$NOW",
            "target_interval_depth_minutes": timedelta(minutes=120),
            "historical_interval_end": "$NOW",
            "historical_interval_depth_minutes": timedelta(hours=6),
            "diagnostic_ids": [
                "DiagnosticEngineSpeedId",
                "DiagnosticEngineRoadSpeedId",
                "DiagnosticDeviceTotalFuelId",
            ],
            "warning_threshold": 0.15,
            "error_threshold": 0.30,
            "segment_proximity_filter": 0.005,
            "validation_type": "ROAD_COUNTER_2h",
            # Done and done. Like Ron Dunn
            # https://www.youtube.com/watch?v=5B29xg3aMXw
            "done": "DONE",
        },
    },
    "road-counter-realtime": {
        "script_folder": "road-counter",
        "params": {
            "target_interval_end": "$NOW",
            "target_interval_depth_minutes": timedelta(minutes=15),
            "historical_interval_end": datetime(
                year=2026, month=2, day=22, hour=16, tzinfo=timezone.utc
            ),
            "historical_interval_depth_minutes": timedelta(hours=6),
            "diagnostic_ids": ["DiagnosticEngineRoadSpeedId"],
            "warning_threshold": 0.15,
            "error_threshold": 0.30,
            "segment_proximity_filter": 0.005,
            "validation_type": "ROAD_COUNTER_REALTIME",
            "done": "DONE",
        },
    },
}


def get_database_url(environ: Mapping[str, str]) -> str:
    """Retrieves and validates the database URL from environment variables."""
    database_url = environ.get("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is required")
    parsed = urlparse(database_url)
    if parsed.scheme not in ("postgresql", "postgres"):
        raise ValueError(
            f"DATABASE_URL must be a valid PostgreSQL URL (got scheme: {parsed.scheme!r})"
        )
    if not parsed.hostname:
        raise ValueError("DATABASE_URL must include a host")
    if not parsed.path or parsed.path == "/":
        raise ValueError("DATABASE_URL must include a database name")
    return database_url


def _resolve_param_markers(params: Mapping[str, Any]) -> dict[str, Any]:
    """Resolves special parameter markers like $NOW to actual values."""

    resolved = {}
    for key, val in params.items():
        if val == "$NOW":
            resolved[key] = datetime.now(tz=timezone.utc).replace(
                second=0, microsecond=0
            )
        else:
            resolved[key] = val

    return resolved


def convert_sql_params(sql: str, params: Mapping[str, Any]) -> tuple[str, list[Any]]:
    values = []
    # Map parameter name -> its $N position
    name_to_index = {}

    def replace(match):
        name = match.group(1).strip()
        if name not in params:
            raise KeyError(f"SQL requires '{name}', but it's missing in params")

        if name not in name_to_index:
            values.append(params[name])
            name_to_index[name] = len(values)  # 1-based index for $N

        return f"${name_to_index[name]}"

    # Crucial: Use re.DOTALL and ensure we match the right pattern
    new_sql = re.sub(r"%\((.*?)\)s", replace, sql, flags=re.DOTALL)

    # If values is empty but the SQL still has $ signs,
    # it means the regex didn't find anything to replace!
    return new_sql, values


async def has_recent_locations(db_url: str, window_minutes: int = 15) -> bool:
    """Checks if there are any location records in the last `window_minutes` minutes."""

    from_dt = datetime.now(tz=timezone.utc) - timedelta(minutes=window_minutes)
    try:
        conn = await asyncpg.connect(dsn=db_url)
        try:
            val = await conn.fetchval(
                "SELECT 1 FROM geotab_location WHERE datetime >= $1 LIMIT 1", from_dt
            )
            return val is not None
        finally:
            await conn.close()
    except Exception as e:
        logger.error(f"Pre-flight check failed: {e}")

        return False


def load_scripts(scripts_dir: Path, checks: Mapping[str, Mapping[str, Any]]):
    """Loads SQL scripts for each check based on the provided configuration."""

    scripts = []
    for check_name, check_config in checks.items():
        folder_name = check_config.get("script_folder", check_name)
        check_dir = scripts_dir / folder_name
        if not check_dir.exists():
            raise FileNotFoundError(
                f"Check directory not found: {check_dir} (for check '{check_name}')"
            )
        sql_files = sorted(check_dir.glob("*.sql"))
        if not sql_files:
            raise FileNotFoundError(f"No SQL files found in {check_dir}")
        stages = [(f.name, f.read_text()) for f in sql_files]
        scripts.append((check_name, stages, check_config.get("params", {})))

    return scripts


async def run_check_async(
    pool: asyncpg.Pool,
    check_name: str,
    stages: list[tuple[str, str]],
    params: Mapping[str, Any],
) -> dict[str, Any]:
    total_rows = 0
    async with pool.acquire() as conn:
        async with conn.transaction():
            for _, sql in stages:
                # 1. Get the converted SQL and values list
                converted_sql, values = convert_sql_params(sql, params)

                if "SELECT" in converted_sql.upper():
                    # 2. Pass the values list using unpacking *values
                    rows = await conn.fetch(converted_sql, *values)
                    total_rows += len(rows)
                else:
                    # 3. Here too, we must unpack *values
                    status = await conn.execute(converted_sql, *values)
                    try:
                        if " " in status:
                            total_rows += int(status.split()[-1])
                    except (ValueError, IndexError):
                        pass

    return {
        "check": check_name,
        "status": "ok",
        "rows": total_rows,
        "stages": len(stages),
    }


async def run_once_async(scripts_dir: Path, db_url: str) -> int:
    """Runs all checks once and returns 0 if all passed, 1 if any failed."""

    if not await has_recent_locations(db_url):
        logger.info("Skipping: no new data in last 15m")
        return 0

    scripts = load_scripts(scripts_dir, CHECKS)

    async with asyncpg.create_pool(dsn=db_url, min_size=1, max_size=20) as pool:
        tasks = []
        for name, stages, params in scripts:
            resolved = _resolve_param_markers(params)
            tasks.append(run_check_async(pool, name, stages, resolved))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        failed = 0
        for res in results:
            if isinstance(res, Exception):
                logger.error(f"Check execution error: {res}")
                failed += 1
            elif res.get("status") == "failed":
                failed += 1
            else:
                logger.info(f"OK: {res['check']} ({res['rows']} rows)")

        return 1 if failed > 0 else 0


async def main(
    scripts_dir: Path = Path("./scripts"),
    environ: Mapping[str, str] | None = None,
) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    environ = environ or os.environ

    try:
        db_url = get_database_url(environ)
    except ValueError as e:
        logger.error(f"Database URL error: {e}")
        return 1

    interval_str = environ.get("CHECK_INTERVAL_SECONDS")
    if interval_str is None:
        return await run_once_async(scripts_dir, db_url)

    interval_seconds = int(interval_str)
    logger.info(f"Scheduler started: {interval_seconds}s interval")

    while True:
        exit_code = await run_once_async(scripts_dir, db_url)
        if exit_code != 0:
            logger.warning("One or more checks failed")
        await asyncio.sleep(interval_seconds)


if __name__ == "__main__":
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        logger.info("Service stopped by user")
