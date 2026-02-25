"""Check-runner service. Periodically runs SQL scripts from check-scripts folder."""

import logging
import os
import sys
from collections.abc import Callable, Mapping
from concurrent.futures import Executor, ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from datetime import timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from psycopg2 import pool as psycopg2_pool
from psycopg2.extensions import connection as PgConnection

logger = logging.getLogger("check-runner")

# Type alias: check name -> list of (stage_name, sql)
CheckScript = tuple[str, list[tuple[str, str]]]


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
    context: Mapping[str, Any],
) -> dict[str, Any]:
    """Run a multi-stage SQL check. All stages execute in one transaction."""
    total_rows = 0

    with conn.cursor() as cur:
        for stage_name, sql in stages:
            try:
                cur.execute(sql, context)
            except KeyError as e:
                param = str(e).strip("'")
                raise ValueError(f"Missing parameter: '{param}'") from None

            if cur.description:
                total_rows += len(cur.fetchall())
            else:
                total_rows += cur.rowcount

    conn.commit()
    return {"check": check_name, "status": "ok", "rows": total_rows, "stages": len(stages)}


@contextmanager
def db_connection_pool(dsn: str, minconn: int = 1, maxconn: int = 20) -> Any:
    pool = psycopg2_pool.ThreadedConnectionPool(minconn=minconn, maxconn=maxconn, dsn=dsn)
    try:
        yield pool
    finally:
        pool.closeall()


def run_all_checks(
    executor: Executor,
    pool: Any,
    scripts: list[CheckScript],
    contexts: Mapping[str, Mapping[str, Any]],
) -> int:
    """Run all check scripts. Returns number of failed checks."""
    logger.info(f"Running {len(scripts)} check(s)")

    def _run_single(
        name: str, stages: list[tuple[str, str]], context: Mapping[str, Any]
    ) -> dict[str, Any]:
        conn = None
        try:
            conn = pool.getconn()
            return run_check(conn, name, stages, context)
        except Exception as e:
            logger.error(f"{name} failed: {e}")
            return {"check": name, "status": "failed", "error": str(e)}
        finally:
            if conn is not None:
                pool.putconn(conn)

    futures = [
        executor.submit(_run_single, name, stages, contexts.get(name, {}))
        for name, stages in scripts
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


def load_scripts(scripts_dir: Path) -> list[CheckScript]:
    """Load SQL scripts from directories.

    Each directory represents one check. SQL files within a directory are
    executed as stages, sorted by filename.
    """
    scripts: list[CheckScript] = []

    for path in sorted(scripts_dir.iterdir()):
        if not path.is_dir():
            continue
        sql_files = sorted(path.glob("*.sql"))
        if not sql_files:
            continue
        stages = [(f.name, f.read_text()) for f in sql_files]
        scripts.append((path.name, stages))

    return scripts


def main(
    scripts_dir: Path = Path("./check-scripts"),
    environ: Mapping[str, str] | None = None,
    max_workers: int = 20,
    executor_factory: Callable[..., Executor] | None = None,
    pool_factory: Callable[..., Any] | None = None,
) -> int:
    """Entry point. Returns exit code (0 for success, 1 for failure)."""
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

    contexts: Mapping[str, Mapping[str, Any]] = {
        "distance_to_road_validation": {
            "interval": timedelta(minutes=60),
            "warning_threshold": 5,
            "error_threshold": 10,
        },
    }

    scripts = load_scripts(scripts_dir)
    if not scripts:
        logger.error(f"No SQL scripts found in {scripts_dir}, nothing to run")
        return 1

    try:
        db_url = get_database_url(environ)
    except ValueError as e:
        logger.error(f"Invalid DATABASE_URL: {e}")
        return 1

    with executor_factory(max_workers=max_workers) as executor:
        with pool_factory(dsn=db_url, minconn=1, maxconn=max_workers) as pool:
            failed = run_all_checks(executor, pool, scripts, contexts)

    if failed:
        logger.error(f"{failed} check(s) failed")
        return 1

    logger.info("All checks completed successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
