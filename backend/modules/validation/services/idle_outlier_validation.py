import asyncio
from datetime import datetime, timedelta
import os

from sqlalchemy import text

from database.database import SessionLocal
from logging_config import configure_logger
from modules.geotab_database.models.geotab_database import GeotabDatabase  # noqa: F401
from modules.geotab_location.enums import ValidationStatus
from modules.utils.utils import require_recent_data
from modules.validation.models.validation import Validation

logger = configure_logger(__name__)

VALIDATION_TYPE = "IDLE_OUTLIER"

DBSCAN_EPS_METERS = 15
DBSCAN_MIN_POINTS = 300
CLUSTER_WINDOW_HOURS = 24
RECENT_WINDOW_MINUTES = int(os.getenv("RECENT_WINDOW_MINUTES", "15"))


@require_recent_data
async def run_single_idle_outlier_validation() -> None:
    """Run a single idle-outlier validation pass.

    For recent idle points, stores row-level classification in
    `idle_outlier_results.is_outlier`:
      - true  => DBSCAN noise point (outlier)
      - false => belongs to a DBSCAN cluster (normal)
    """

    run_started_at = datetime.utcnow()
    from_datetime = run_started_at - timedelta(minutes=RECENT_WINDOW_MINUTES)
    cluster_from_datetime = run_started_at - timedelta(hours=CLUSTER_WINDOW_HOURS)

    async with SessionLocal() as session:
        database_ids_query = text(
            """
            SELECT DISTINCT geotab_database_id
            FROM geotab_location
            WHERE datetime >= :cluster_from_datetime
              AND geometry IS NOT NULL
              AND speed = 0
            """
        )
        database_ids_result = await session.execute(
            database_ids_query,
            {"cluster_from_datetime": cluster_from_datetime},
        )
        geotab_database_ids = database_ids_result.scalars().all()

        if not geotab_database_ids:
            logger.info(
                "Idle outlier validation skipped: no databases with recent idle locations"
            )
            return

        insert_results_query = text(
            """
            WITH grouped_idle_24h AS (
                SELECT
                    MIN(id) AS id,
                    datetime,
                    geometry
                FROM geotab_location
                WHERE geotab_database_id = :geotab_database_id
                  AND datetime >= :cluster_from_datetime
                  AND geometry IS NOT NULL
                  AND speed = 0
                GROUP BY device_id, datetime, geometry
            ),
            clustered AS (
                SELECT
                    id,
                    datetime,
                    ST_ClusterDBSCAN(ST_Transform(geometry, 3857), :eps_meters, :min_points)
                        OVER () AS cluster_id
                FROM grouped_idle_24h
            )
            INSERT INTO idle_outlier_results (
                geotab_location_id,
                validation_id,
                is_outlier
            )
            SELECT
                id,
                :validation_id,
                (cluster_id IS NULL)
            FROM clustered
            WHERE datetime >= :from_datetime
            """
        )

        summary_query = text(
            """
            SELECT COUNT(*) AS errors_count
            FROM idle_outlier_results
            WHERE validation_id = :validation_id
              AND is_outlier = TRUE
            """
        )

        total_query = text(
            """
            SELECT COUNT(*) AS total_count
            FROM (
                SELECT 1
                FROM geotab_location
                WHERE datetime >= :from_datetime
                  AND geometry IS NOT NULL
                  AND speed = 0
                  AND geotab_database_id = :geotab_database_id
                GROUP BY device_id, datetime, geometry
            ) grouped_idle_recent
            """
        )

        per_device_query = text(
            """
            WITH totals AS (
                SELECT grouped.device_id, COUNT(*) AS total_count
                FROM (
                    SELECT gl.device_id, gl.datetime, gl.geometry
                    FROM geotab_location gl
                    WHERE gl.datetime >= :from_datetime
                      AND gl.geometry IS NOT NULL
                      AND gl.speed = 0
                      AND gl.geotab_database_id = :geotab_database_id
                    GROUP BY gl.device_id, gl.datetime, gl.geometry
                ) grouped
                GROUP BY grouped.device_id
            ),
            flagged AS (
                SELECT gl.device_id, COUNT(*) AS warning_count
                FROM idle_outlier_results ior
                JOIN geotab_location gl ON gl.id = ior.geotab_location_id
                WHERE ior.validation_id = :validation_id
                  AND ior.is_outlier = TRUE
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
                0,
                COALESCE(flagged.warning_count, 0)
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

            idle_total_result = await session.execute(
                text(
                    """
                    SELECT COUNT(*)
                    FROM (
                        SELECT 1
                        FROM geotab_location
                        WHERE geotab_database_id = :geotab_database_id
                          AND datetime >= :cluster_from_datetime
                          AND geometry IS NOT NULL
                          AND speed = 0
                        GROUP BY device_id, datetime, geometry
                    ) grouped_idle_24h
                    """
                ),
                {
                    "geotab_database_id": geotab_database_id,
                    "cluster_from_datetime": cluster_from_datetime,
                },
            )
            idle_total = idle_total_result.scalar_one()

            idle_recent_result = await session.execute(
                text(
                    """
                    SELECT COUNT(*)
                    FROM (
                        SELECT 1
                        FROM geotab_location
                        WHERE geotab_database_id = :geotab_database_id
                          AND datetime >= :from_datetime
                          AND geometry IS NOT NULL
                          AND speed = 0
                        GROUP BY device_id, datetime, geometry
                    ) grouped_idle_recent
                    """
                ),
                {
                    "geotab_database_id": geotab_database_id,
                    "from_datetime": from_datetime,
                },
            )
            idle_recent = idle_recent_result.scalar_one()
            logger.info(
                "geotab_database_id=%s: idle points — 24h window: %s, recent %s min: %s",
                geotab_database_id,
                idle_total,
                RECENT_WINDOW_MINUTES,
                idle_recent,
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
                    "geotab_database_id": geotab_database_id,
                    "cluster_from_datetime": cluster_from_datetime,
                    "from_datetime": from_datetime,
                    "eps_meters": DBSCAN_EPS_METERS,
                    "min_points": DBSCAN_MIN_POINTS,
                    "validation_id": validation_id,
                },
            )

            inserted_result = await session.execute(
                text(
                    "SELECT COUNT(*) FROM idle_outlier_results WHERE validation_id = :validation_id"
                ),
                {"validation_id": validation_id},
            )
            inserted_count = inserted_result.scalar_one()
            logger.info(
                "geotab_database_id=%s: inserted %s classified idle rows into idle_outlier_results",
                geotab_database_id,
                inserted_count,
            )

            await session.execute(
                per_device_query,
                {
                    "from_datetime": from_datetime,
                    "geotab_database_id": geotab_database_id,
                    "validation_id": validation_id,
                },
            )

            summary_result = await session.execute(
                summary_query,
                {"validation_id": validation_id},
            )
            errors_count = summary_result.scalar_one()

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
            validation.warnings = 0
            validation.errors = errors_count
            validation.total = total_count

            logger.info(
                "Idle outlier validation %s completed for geotab_database_id=%s: errors=%s",
                validation_id,
                geotab_database_id,
                errors_count,
            )

        await session.commit()


async def run_idle_outlier_validation_service(interval_seconds: int = 300) -> None:
    while True:
        try:
            await run_single_idle_outlier_validation()
        except Exception:
            logger.exception("Idle outlier validation run failed")

        await asyncio.sleep(interval_seconds)
