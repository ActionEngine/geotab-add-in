#!/usr/bin/env python3
"""Read-only check-runner service. Periodically runs SQL scripts from check-scripts folder."""

import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, Mapping
from urllib.parse import urlparse

import psycopg2
from psycopg2 import pool

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("check-runner")

MAX_WORKERS = 20


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

    print('=' * 100)
    print(database_url, flush=True)
    return database_url


def _create_connection_pool(dsn: str) -> pool.ThreadedConnectionPool:
    return psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=MAX_WORKERS, dsn=dsn)


DATABASE_URL = get_database_url(os.environ)
db_pool = _create_connection_pool(DATABASE_URL)


def run_check(script_path: Path, context: Dict) -> Dict:
    """Run a single SQL check script with named parameters."""
    sql = script_path.read_text()
    conn = db_pool.getconn()

    try:
        with conn.cursor() as cur:
            try:
                cur.execute(sql, context)
            except KeyError as e:
                param = str(e).strip("'")
                raise ValueError(f"Missing parameter: '{param}'") from None

            rows = cur.fetchall() if cur.description else []
            return {"script": script_path.name, "status": "ok", "rows": len(rows)}

    except Exception as e:
        logger.error(f"{script_path.name} failed: {e}")
        return {"script": script_path.name, "status": "failed", "error": str(e)}
    finally:
        db_pool.putconn(conn)


def run_all_checks(scripts_dir: Path, contexts: Dict[str, Dict]) -> int:
    """Run all SQL scripts in the directory. Returns number of failed checks."""
    scripts = sorted(scripts_dir.glob("*.sql"))
    if not scripts:
        logger.warning(f"No SQL scripts found in {scripts_dir}")
        return 0

    logger.info(f"Running {len(scripts)} check scripts with {MAX_WORKERS} workers")

    failed = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(run_check, s, contexts.get(s.name, {})): s
            for s in scripts
        }

        for future in as_completed(futures):
            result = future.result()
            if result["status"] == "failed":
                failed += 1
                logger.error(f"FAILED: {result['script']} - {result.get('error')}")
            else:
                logger.info(f"OK: {result['script']} ({result['rows']} rows)")

    return failed


def main():
    scripts_dir = Path("/app/check-scripts")
    contexts: Dict[str, Dict] = {}

    failed = run_all_checks(scripts_dir, contexts)

    if failed:
        logger.error(f"{failed} check(s) failed")
        sys.exit(1)

    logger.info("All checks completed successfully")


if __name__ == "__main__":
    main()
