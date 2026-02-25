"""Integration tests for SQL check scripts."""

import os
from datetime import timedelta
from pathlib import Path

import psycopg2
import pytest

from check_runner import load_scripts


def test_distance_to_road_validation_with_data():
    """Test distance_to_road_validation check with proper test data."""
    database_url = os.environ["DATABASE_URL"]

    scripts_dir = Path("check-scripts")
    checks = {name: stages for name, stages in load_scripts(scripts_dir)}
    stages = checks.get("distance_to_road_validation", [])

    with psycopg2.connect(database_url) as conn:
        conn.rollback()

        with conn.cursor() as cur:
            cur.execute("SELECT id FROM geotab_database LIMIT 1")
            row = cur.fetchone()

            if row is None:
                pytest.skip("No geotab_database found - create one to run this test")

            db_id = row[0]

            cur.execute(
                """
                INSERT INTO geotab_location
                    (datetime, device_id, external_id, geometry, speed, geotab_database_id)
                VALUES
                    (NOW(), 'test_device', 'test123', ST_SetSRID(ST_MakePoint(0, 0), 4326), 50, %s),
                    (NOW(), 'test_device', 'test123', ST_SetSRID(ST_MakePoint(0.001, 0.001), 4326), 50, %s)
                RETURNING id
                """,
                (db_id, db_id),
            )
            location_ids = [r[0] for r in cur.fetchall()]

            cur.execute(
                """
                INSERT INTO overture_segments
                    (external_id, geometry, bbox, geotab_database_id)
                VALUES
                    ('test_road', ST_SetSRID(ST_MakeLine(ST_MakePoint(0, 0), ST_MakePoint(0.01, 0)), 4326),
                     '[0,0,0.01,0]'::jsonb, %s)
                """,
                (db_id,),
            )

            from datetime import timedelta

            params = {
                "interval": timedelta(minutes=15),
                "warning_threshold": 5,
                "error_threshold": 10,
            }

            # Execute all stages - temp table from stage 02 is available to stages 03-05
            for stage_name, sql in stages:
                cur.execute(sql, params)

        conn.rollback()


def test_select_device_statuses_with_data():
    """Test select_device_statuses check runs without errors."""
    database_url = os.environ["DATABASE_URL"]

    scripts_dir = Path("check-scripts")
    checks = {name: stages for name, stages in load_scripts(scripts_dir)}
    stages = checks.get("select_device_statuses", [])

    if not stages:
        pytest.skip("No stages found for select_device_statuses")

    with psycopg2.connect(database_url) as conn:
        conn.rollback()

        with conn.cursor() as cur:
            params = {
                "interval": timedelta(minutes=15),
                "warning_threshold": 5,
                "error_threshold": 10,
            }

            for stage_name, sql in stages:
                cur.execute(sql, params)

        conn.rollback()
