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
# Speed thresholds for teleportation detection.
# Tracked vehicles (trucks, vans) typically travel up to ~120 km/h.
# GPS noise alone can produce apparent speeds of ~50–80 km/h at 1-second intervals,
# so both thresholds are set well above that noise floor to avoid false positives.
# WARNING: implied speed is suspiciously high but could still be a GPS glitch.
# ERROR:   speed is physically impossible for any road vehicle — clear teleportation jump.

# These thresholds can be tuned based on the specific use case and data characteristics.
# ST_Distance(...::geography) → returns distance in meters;
# EXTRACT(EPOCH FROM ...) → returns seconds;
# dividing gives m/s, multiplying by 3.6 converts to km/h  (3600 s/h ÷ 1000 m/km).
WARNING_THRESHOLD_KMH = 100  # well above GPS noise for vehicles up to ~120 km/h
ERROR_THRESHOLD_KMH = 200  # clear GPS teleportation jump


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
                    -- Compute implied speed between consecutive points of the same device.
                    -- ST_Distance(...::geography) returns meters; EXTRACT(EPOCH FROM ...) returns seconds.
                    -- Dividing gives m/s, multiplying by 3.6 converts to km/h (3600 s/h ÷ 1000 m/km).
                    -- NULLIF guards against division by zero when two points share the same timestamp.
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

        per_device_query = text(
            """
            WITH totals AS (
                SELECT gl.device_id, COUNT(*) AS total_count
                FROM geotab_location gl
                WHERE gl.datetime >= :from_datetime
                  AND gl.geometry IS NOT NULL
                  AND gl.geotab_database_id = :geotab_database_id
                GROUP BY gl.device_id
            ),
            flagged AS (
                SELECT
                    gl.device_id,
                    COUNT(*) FILTER (
                        WHERE tr.implied_speed_kmh > :warning_threshold
                          AND tr.implied_speed_kmh <= :error_threshold
                    ) AS warning_count,
                    COUNT(*) FILTER (
                        WHERE tr.implied_speed_kmh > :error_threshold
                    ) AS error_count
                FROM teleportation_results tr
                JOIN geotab_location gl ON gl.id = tr.geotab_location_id
                WHERE tr.validation_id = :validation_id
                GROUP BY gl.device_id
            )
            INSERT INTO validation_results_by_device (
                validation_id,
                device_id,
                total,
                warnings,
                errors
            )
            SELECT
                :validation_id,
                totals.device_id,
                totals.total_count,
                COALESCE(flagged.warning_count, 0),
                COALESCE(flagged.error_count, 0)
            FROM totals
            LEFT JOIN flagged ON flagged.device_id = totals.device_id
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

            await session.execute(
                per_device_query,
                {
                    "from_datetime": from_datetime,
                    "geotab_database_id": geotab_database_id,
                    "validation_id": validation_id,
                    "warning_threshold": WARNING_THRESHOLD_KMH,
                    "error_threshold": ERROR_THRESHOLD_KMH,
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
