"""Check-runner service. Periodically runs SQL scripts from check-scripts folder."""

import logging
import os
import sys
from concurrent.futures import Executor, ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Mapping
from urllib.parse import urlparse

import psycopg2
from psycopg2 import pool as psycopg2_pool
from psycopg2.extensions import connection as PgConnection

logger = logging.getLogger("check-runner")


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
    script_name: str,
    sql: str,
    context: Mapping[str, Any],
) -> dict[str, Any]:
    """Run a single SQL check script with named parameters."""
    with conn.cursor() as cur:
        try:
            cur.execute(sql, context)
        except KeyError as e:
            param = str(e).strip("'")
            raise ValueError(f"Missing parameter: '{param}'") from None

        rows = cur.fetchall() if cur.description else []
        return {"script": script_name, "status": "ok", "rows": len(rows)}


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
    scripts: list[tuple[str, str]],
    contexts: Mapping[str, Mapping[str, Any]],
) -> int:
    """Run all SQL scripts. Returns number of failed checks."""
    logger.info(f"Running {len(scripts)} check scripts")

    def _run_single(name: str, sql: str, context: Mapping[str, Any]) -> dict[str, Any]:
        conn = None
        try:
            conn = pool.getconn()
            return run_check(conn, name, sql, context)
        except Exception as e:
            logger.error(f"{name} failed: {e}")
            return {"script": name, "status": "failed", "error": str(e)}
        finally:
            if conn is not None:
                pool.putconn(conn)

    futures = [
        executor.submit(_run_single, name, sql, contexts.get(name, {}))
        for name, sql in scripts
    ]

    failed = 0
    for future in as_completed(futures):
        result = future.result()
        if result["status"] == "failed":
            failed += 1
            logger.error(f"FAILED: {result['script']} - {result.get('error')}")
        else:
            logger.info(f"OK: {result['script']} ({result['rows']} rows)")

    return failed


def load_scripts(scripts_dir: Path) -> list[tuple[str, str]]:
    scripts = sorted(scripts_dir.glob("*.sql"))
    return [(s.name, s.read_text()) for s in scripts]


def main(
    scripts_dir: Path = Path("/app/check-scripts"),
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

    contexts: Mapping[str, Mapping[str, Any]] = {
        # "check1.sql": {"param1": "value1"},
        # "check2.sql": {"paramA": "valueA", "paramB": "valueB"},
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

    executor_factory = executor_factory or ThreadPoolExecutor
    pool_factory = pool_factory or db_connection_pool

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
