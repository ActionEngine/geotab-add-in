import asyncio
import logging
from datetime import datetime, timedelta

from sqlalchemy import text

from database.database import SessionLocal
from modules.geotab_database.models.geotab_database import GeotabDatabase  # noqa: F401
from modules.geotab_location.enums import ValidationStatus
from modules.validation.models.validation import Validation

logger = logging.getLogger(__name__)

VALIDATION_TYPE = "TELEPORTATION"
WARNING_THRESHOLD_KMH = 250  # well above GPS noise for vehicles up to ~120 km/h
ERROR_THRESHOLD_KMH = 500  # clear GPS teleportation jump


async def run_single_teleportation_validation() -> None:
    """Run a single teleportation validation."""

    run_started_at = datetime.utcnow()
    from_datetime = run_started_at - timedelta(minutes=15)

    async with SessionLocal() as session:
        database_ids_query = text(
            """
            SELECT DISTINCT geotab_database_id
            FROM geotab_location
            WHERE datetime >= :from_datetime
              AND geometry IS NOT NULL
            """
        )
        database_ids_result = await session.execute(
            database_ids_query,
            {"from_datetime": from_datetime},
        )
        geotab_database_ids = database_ids_result.scalars().all()

        if not geotab_database_ids:
            logger.info(
                "Teleportation validation skipped: no databases with recent locations"
            )
            return

        insert_results_query = text(
            """
            WITH recent_locations AS (
                SELECT
                    id,
                    device_id,
                    datetime,
                    geometry,
                    LAG(geometry) OVER (
                        PARTITION BY device_id ORDER BY datetime
                    ) AS prev_geometry,
                    LAG(datetime) OVER (
                        PARTITION BY device_id ORDER BY datetime
                    ) AS prev_datetime
                FROM geotab_location
                WHERE datetime >= :from_datetime
                  AND geometry IS NOT NULL
                  AND geotab_database_id = :geotab_database_id
            ),
            speeds AS (
                SELECT
                    id,
                    ST_Distance(geometry::geography, prev_geometry::geography)
                        / NULLIF(EXTRACT(EPOCH FROM (datetime - prev_datetime)), 0) * 3.6
                        AS implied_speed_kmh
                FROM recent_locations
                WHERE prev_geometry IS NOT NULL
            )
            INSERT INTO teleportation_results (implied_speed_kmh, geotab_location_id, validation_id)
            SELECT implied_speed_kmh, id, :validation_id
            FROM speeds
            WHERE implied_speed_kmh > :warning_threshold
            """
        )

        summary_query = text(
            """
            SELECT
                COUNT(*) FILTER (
                    WHERE implied_speed_kmh > :warning_threshold
                    AND implied_speed_kmh <= :error_threshold
                ) AS warning_count,
                COUNT(*) FILTER (
                    WHERE implied_speed_kmh > :error_threshold
                ) AS error_count
            FROM teleportation_results
            WHERE validation_id = :validation_id
            """
        )

        total_query = text(
            """
            SELECT COUNT(*) AS total_count
            FROM (
                SELECT id
                FROM geotab_location
                WHERE datetime >= :from_datetime
                  AND geometry IS NOT NULL
                  AND geotab_database_id = :geotab_database_id
            ) AS candidates
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
                    "validation_type": VALIDATION_TYPE,
                    "geotab_database_id": geotab_database_id,
                },
            )

            validation = Validation(
                geotab_database_id=geotab_database_id,
                started_at=datetime.utcnow(),
                validation_type=VALIDATION_TYPE,
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
                    "warning_threshold": WARNING_THRESHOLD_KMH,
                },
            )

            summary_result = await session.execute(
                summary_query,
                {
                    "validation_id": validation_id,
                    "warning_threshold": WARNING_THRESHOLD_KMH,
                    "error_threshold": ERROR_THRESHOLD_KMH,
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
                "Teleportation validation %s completed for geotab_database_id=%s: warnings=%s, errors=%s",
                validation_id,
                geotab_database_id,
                warning_count,
                error_count,
            )

        await session.commit()


async def run_teleportation_validation_service(interval_seconds: int = 300) -> None:
    while True:
        try:
            await run_single_teleportation_validation()
        except Exception:
            logger.exception("Teleportation validation run failed")

        await asyncio.sleep(interval_seconds)
