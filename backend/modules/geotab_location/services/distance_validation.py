import asyncio
import logging
from datetime import datetime, timedelta

from sqlalchemy import text

from database.database import SessionLocal
from modules.geotab_database.models.geotab_database import GeotabDatabase  # noqa: F401
from modules.geotab_location.enums import ValidationStatus
from modules.geotab_location.models.validation import Validation

logger = logging.getLogger(__name__)


async def run_single_distance_validation() -> None:
    run_started_at = datetime.utcnow()
    from_datetime = run_started_at - timedelta(minutes=15)

    async with SessionLocal() as session:
        database_ids_query = text(
            """
            SELECT DISTINCT gl.geotab_database_id
            FROM geotab_location gl
            WHERE gl.datetime >= :from_datetime
              AND gl.geometry IS NOT NULL
              AND EXISTS (
                  SELECT 1
                  FROM overture_segments os
                  WHERE os.geotab_database_id = gl.geotab_database_id
              )
            """
        )
        database_ids_result = await session.execute(
            database_ids_query,
            {"from_datetime": from_datetime},
        )
        geotab_database_ids = database_ids_result.scalars().all()

        if not geotab_database_ids:
            logger.info("Distance validation skipped: no databases with recent locations")
            return

        insert_results_query = text(
            """
            WITH recent_locations AS (
                SELECT id, geotab_database_id, geometry
                FROM geotab_location
                WHERE datetime >= :from_datetime
                  AND geometry IS NOT NULL
                  AND geotab_database_id = :geotab_database_id
            )
            INSERT INTO distance_to_road_results (distance, geotab_location_id, validation_id)
            SELECT
                nearest.distance_meters,
                gl.id,
                :validation_id
            FROM recent_locations gl
            CROSS JOIN LATERAL (
                SELECT ST_Distance(gl.geometry::geography, os.geometry::geography) AS distance_meters
                FROM overture_segments os
                WHERE os.geotab_database_id = gl.geotab_database_id
                ORDER BY os.geometry <-> gl.geometry
                LIMIT 1
            ) AS nearest
            WHERE nearest.distance_meters > :warning_threshold
            """
        )

        summary_query = text(
            """
            SELECT
                COUNT(*) FILTER (
                    WHERE distance > :warning_threshold
                    AND distance <= :error_threshold
                ) AS warning_count,
                COUNT(*) FILTER (
                    WHERE distance > :error_threshold
                ) AS error_count
            FROM distance_to_road_results
            WHERE validation_id = :validation_id
            """
        )

        total_query = text(
            """
            SELECT COUNT(*) AS total_count
            FROM geotab_location gl
            WHERE gl.datetime >= :from_datetime
              AND gl.geometry IS NOT NULL
              AND gl.geotab_database_id = :geotab_database_id
              AND EXISTS (
                  SELECT 1
                  FROM overture_segments os
                  WHERE os.geotab_database_id = gl.geotab_database_id
              )
            """
        )
        for geotab_database_id in geotab_database_ids:
            await session.execute(
                text(
                    """
                    DELETE FROM validation
                    WHERE validation_type = :validation_type
                      AND geotab_database_id = :geotab_database_id
                    """
                ),
                {
                    "validation_type": "DISTANCE_TO_ROAD",
                    "geotab_database_id": geotab_database_id,
                },
            )

            validation = Validation(
                geotab_database_id=geotab_database_id,
                started_at=datetime.utcnow(),
                validation_type="DISTANCE_TO_ROAD",
                status=ValidationStatus.IN_PROGRESS,
            )
            session.add(validation)
            await session.flush()

            validation_id = validation.id

            await session.execute(
                insert_results_query,
                {
                    "from_datetime": from_datetime,
                    "geotab_database_id": geotab_database_id,
                    "validation_id": validation_id,
                    "warning_threshold": 5,
                },
            )

            summary_result = await session.execute(
                summary_query,
                {
                    "validation_id": validation_id,
                    "warning_threshold": 5,
                    "error_threshold": 10,
                },
            )
            warning_count, error_count = summary_result.one()

            total_result = await session.execute(
                total_query,
                {
                    "from_datetime": from_datetime,
                    "geotab_database_id": geotab_database_id,
                },
            )
            total_count = total_result.scalar_one()

            validation.status = ValidationStatus.DONE
            validation.finished_at = datetime.utcnow()
            validation.warnings = warning_count
            validation.errors = error_count
            validation.total = total_count

            logger.info(
                "Distance validation %s completed for geotab_database_id=%s: warnings=%s, errors=%s",
                validation_id,
                geotab_database_id,
                warning_count,
                error_count,
            )

        await session.commit()


async def run_distance_validation_service(interval_seconds: int = 300) -> None:
    while True:
        try:
            await run_single_distance_validation()
        except Exception:
            logger.exception("Distance validation run failed")

        await asyncio.sleep(interval_seconds)
