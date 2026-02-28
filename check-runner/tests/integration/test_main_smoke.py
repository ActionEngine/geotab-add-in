"""Smoke tests for main() with real database."""

import asyncio
import os
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import psycopg2
from psycopg2.extras import Json

from check_runner import main


def test_main_road_counter_tmp_runs_without_error():
    database_url = os.environ["DATABASE_URL"]
    test_db_name = f"test_db_{uuid.uuid4().hex[:8]}"

    now = datetime.now(tz=timezone.utc).replace(second=0, microsecond=0)
    historical_last_moment = now - timedelta(days=1)

    with psycopg2.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO geotab_database (email, database_name, credentials, ingestion_status)
                VALUES ('test@example.com', %s, 'encrypted_creds', 'none')
                RETURNING id
                """,
                (test_db_name,),
            )
            db_id = cur.fetchone()[0]

        conn.commit()

        test_checks = {
            "road-counter-2hr": {
                "script_folder": "road-counter",
                "params": {
                    "target_interval_end": now,
                    "target_interval_depth_minutes": timedelta(minutes=120),
                    "historical_interval_end": historical_last_moment,
                    "historical_interval_depth_minutes": timedelta(hours=6),
                    "diagnostic_ids": ["DiagnosticEngineSpeedId"],
                    "warning_threshold": 0.30,
                    "error_threshold": 0.50,
                    "segment_proximity_filter": 0.005,
                    "validation_type": "ROAD_COUNTER_ANOMALY",
                    "done": "DONE",
                },
            }
        }

        exit_code = 1
        try:
            with patch.dict(os.environ, {"DATABASE_URL": database_url}):
                with patch("check_runner.CHECKS", test_checks):
                    exit_code = asyncio.run(main(scripts_dir=Path("scripts")))
        finally:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM validation WHERE geotab_database_id = %s", (db_id,))
                cur.execute("DELETE FROM geotab_database WHERE id = %s", (db_id,))
            conn.commit()

        assert exit_code == 0
