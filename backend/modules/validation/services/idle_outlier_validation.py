import asyncio
import logging
from datetime import datetime, timedelta

from sqlalchemy import text

from database.database import SessionLocal
from modules.geotab_database.models.geotab_database import GeotabDatabase  # noqa: F401
from modules.geotab_location.enums import ValidationStatus
from modules.validation.models.validation import Validation

logger = logging.getLogger(__name__)

VALIDATION_TYPE = "IDLE_OUTLIER"

# A vehicle is considered idle when its reported speed is at or below this value.
# Geotab stores speed in km/h. A small non-zero threshold (5 km/h) absorbs
# GPS drift that keeps reporting a tiny speed even when the vehicle is stationary.
IDLE_SPEED_THRESHOLD_KMH = 5

# DBSCAN parameters for clustering idle points.
#
# EPS_METERS: radius of a neighbourhood in meters. 50 m covers a typical
# intersection, bus stop, or traffic-light zone without merging adjacent stops.
#
# MIN_POINTS: minimum idle stops that must fall within EPS_METERS of each other
# to form a cluster (= a known stop location). 3 is a conservative floor — if
# at least 3 separate stops happened at roughly the same spot over the past day,
# we treat it as a legitimate idle cluster (traffic light, junction, etc.).
# Points that don't belong to any cluster get cluster_id = NULL → outliers.
#
# Resource note: DBSCAN is run on idle-only points (speed ≤ threshold), which
# is a small fraction of all location records. Geometries are projected to
# EPSG:3857 (Web Mercator, unit = metres) so EPS can be specified directly in
# metres without degree-to-metre conversion.
DBSCAN_EPS_METERS = 50
DBSCAN_MIN_POINTS = 3

# How far back to look when building idle clusters (to capture enough stops
# at recurring locations like traffic lights).
CLUSTER_WINDOW_HOURS = 24

# How far back to look for *recent* idle points to flag as outliers.
# Only the most recent window is written to idle_outlier_results so the
# validation table stays focused on current anomalies.
RECENT_WINDOW_MINUTES = 15


async def run_single_idle_outlier_validation() -> None:
    """Run a single idle-outlier validation pass.

    Strategy
    --------
    1. Collect all idle points for the past CLUSTER_WINDOW_HOURS to give
       DBSCAN enough data to identify recurring stop locations.
    2. Run ST_ClusterDBSCAN (projected to EPSG:3857 for metre-based EPS) over
       those points partitioned per database — no per-device partitioning,
       because clusters emerge from *multiple* devices stopping at the *same*
       physical location (traffic lights, junctions).
    3. Points whose cluster_id IS NULL are outliers — they stopped somewhere
       that no other vehicle (or no previous trip) has stopped before.
    4. Only the subset that falls inside the RECENT_WINDOW_MINUTES are inserted
       into idle_outlier_results; older outliers are ignored to keep the
       validation fresh.
    """

    run_started_at = datetime.utcnow()
    from_datetime = run_started_at - timedelta(minutes=RECENT_WINDOW_MINUTES)
    cluster_from_datetime = run_started_at - timedelta(hours=CLUSTER_WINDOW_HOURS)

    async with SessionLocal() as session:
        # Look for databases that have idle points in the CLUSTER window (24 h),
        # not just the recent window — so we don't silently skip when there are
        # no fresh idle points but clusters/outliers still exist from earlier.
        database_ids_query = text(
            """
            SELECT DISTINCT geotab_database_id
            FROM geotab_location
            WHERE datetime >= :cluster_from_datetime
              AND geometry IS NOT NULL
              AND speed <= :idle_speed_threshold
            """
        )
        database_ids_result = await session.execute(
            database_ids_query,
            {
                "cluster_from_datetime": cluster_from_datetime,
                "idle_speed_threshold": IDLE_SPEED_THRESHOLD_KMH,
            },
        )
        geotab_database_ids = database_ids_result.scalars().all()

        if not geotab_database_ids:
            logger.info(
                "Idle outlier validation skipped: no databases with recent idle locations"
            )
            return

        # Cluster idle points from the past 24 h, then flag only recent outliers.
        #
        # ST_ClusterDBSCAN window function returns NULL for points that do not
        # belong to any cluster (noise points in DBSCAN terminology) — these are
        # the outlier idle locations we want to flag.
        #
        # We project geometry to EPSG:3857 so that EPS is expressed in metres.
        insert_results_query = text(
            """
            WITH idle_24h AS (
                SELECT
                    id,
                    datetime,
                    ST_Transform(geometry, 3857) AS geom_m
                FROM geotab_location
                WHERE geotab_database_id = :geotab_database_id
                  AND datetime >= :cluster_from_datetime
                  AND geometry IS NOT NULL
                  AND speed <= :idle_speed_threshold
            ),
            clustered AS (
                SELECT
                    id,
                    datetime,
                    ST_ClusterDBSCAN(geom_m, :eps_meters, :min_points)
                        OVER () AS cluster_id
                FROM idle_24h
            )
            INSERT INTO idle_outlier_results (geotab_location_id, validation_id)
            SELECT id, :validation_id
            FROM clustered
            WHERE cluster_id IS NULL
              AND datetime >= :from_datetime
            """
        )

        summary_query = text(
            """
            SELECT COUNT(*) AS warning_count
            FROM idle_outlier_results
            WHERE validation_id = :validation_id
            """
        )

        total_query = text(
            """
            SELECT COUNT(*) AS total_count
            FROM geotab_location
            WHERE datetime >= :from_datetime
              AND geometry IS NOT NULL
              AND speed <= :idle_speed_threshold
              AND geotab_database_id = :geotab_database_id
            """
        )

        per_device_query = text(
            """
            WITH totals AS (
                SELECT gl.device_id, COUNT(*) AS total_count
                FROM geotab_location gl
                WHERE gl.datetime >= :from_datetime
                  AND gl.geometry IS NOT NULL
                  AND gl.speed <= :idle_speed_threshold
                  AND gl.geotab_database_id = :geotab_database_id
                GROUP BY gl.device_id
            ),
            flagged AS (
                SELECT gl.device_id, COUNT(*) AS warning_count
                FROM idle_outlier_results ior
                JOIN geotab_location gl ON gl.id = ior.geotab_location_id
                WHERE ior.validation_id = :validation_id
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
                0
            FROM totals
            LEFT JOIN flagged ON flagged.device_id = totals.device_id
            """
        )

        # Compute convex-hull polygons for each cluster and persist them so
        # MVT tile queries can read pre-built geometries without re-running
        # DBSCAN on every request. DBSCAN is re-run here (same params) because
        # text() queries cannot share CTEs across two separate INSERTs.
        insert_clusters_query = text(
            """
            WITH idle_24h AS (
                SELECT
                    ST_Transform(geometry, 3857) AS geom_m
                FROM geotab_location
                WHERE geotab_database_id = :geotab_database_id
                  AND datetime >= :cluster_from_datetime
                  AND geometry IS NOT NULL
                  AND speed <= :idle_speed_threshold
            ),
            clustered AS (
                SELECT
                    geom_m,
                    ST_ClusterDBSCAN(geom_m, :eps_meters, :min_points)
                        OVER () AS cluster_id
                FROM idle_24h
            ),
            hulls AS (
                SELECT
                    cluster_id,
                    -- Back-project to WGS-84 for storage and tile rendering
                    ST_Transform(
                        ST_ConvexHull(ST_Collect(geom_m)),
                        4326
                    ) AS geometry,
                    COUNT(*) AS point_count
                FROM clustered
                WHERE cluster_id IS NOT NULL
                GROUP BY cluster_id
            )
            INSERT INTO idle_clusters (geotab_database_id, cluster_id, geometry, point_count)
            SELECT :geotab_database_id, cluster_id, geometry, point_count
            FROM hulls
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

            # Replace precomputed clusters for this database
            await session.execute(
                text(
                    "DELETE FROM idle_clusters WHERE geotab_database_id = :geotab_database_id"
                ),
                {"geotab_database_id": geotab_database_id},
            )
            await session.execute(
                insert_clusters_query,
                {
                    "geotab_database_id": geotab_database_id,
                    "cluster_from_datetime": cluster_from_datetime,
                    "idle_speed_threshold": IDLE_SPEED_THRESHOLD_KMH,
                    "eps_meters": DBSCAN_EPS_METERS,
                    "min_points": DBSCAN_MIN_POINTS,
                },
            )

            cluster_count_result = await session.execute(
                text(
                    "SELECT COUNT(*) FROM idle_clusters WHERE geotab_database_id = :geotab_database_id"
                ),
                {"geotab_database_id": geotab_database_id},
            )
            cluster_count = cluster_count_result.scalar_one()
            logger.info(
                "geotab_database_id=%s: built %s idle clusters (eps=%sm, min_points=%s, window=%sh)",
                geotab_database_id,
                cluster_count,
                DBSCAN_EPS_METERS,
                DBSCAN_MIN_POINTS,
                CLUSTER_WINDOW_HOURS,
            )

            # Diagnostic: count total idle points in the 24h window before filtering
            idle_total_result = await session.execute(
                text(
                    """
                    SELECT COUNT(*) FROM geotab_location
                    WHERE geotab_database_id = :geotab_database_id
                      AND datetime >= :cluster_from_datetime
                      AND geometry IS NOT NULL
                      AND speed <= :idle_speed_threshold
                    """
                ),
                {
                    "geotab_database_id": geotab_database_id,
                    "cluster_from_datetime": cluster_from_datetime,
                    "idle_speed_threshold": IDLE_SPEED_THRESHOLD_KMH,
                },
            )
            idle_total = idle_total_result.scalar_one()

            idle_recent_result = await session.execute(
                text(
                    """
                    SELECT COUNT(*) FROM geotab_location
                    WHERE geotab_database_id = :geotab_database_id
                      AND datetime >= :from_datetime
                      AND geometry IS NOT NULL
                      AND speed <= :idle_speed_threshold
                    """
                ),
                {
                    "geotab_database_id": geotab_database_id,
                    "from_datetime": from_datetime,
                    "idle_speed_threshold": IDLE_SPEED_THRESHOLD_KMH,
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
                    "idle_speed_threshold": IDLE_SPEED_THRESHOLD_KMH,
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
                "geotab_database_id=%s: inserted %s outlier rows into idle_outlier_results",
                geotab_database_id,
                inserted_count,
            )

            await session.execute(
                per_device_query,
                {
                    "from_datetime": from_datetime,
                    "geotab_database_id": geotab_database_id,
                    "idle_speed_threshold": IDLE_SPEED_THRESHOLD_KMH,
                    "validation_id": validation_id,
                },
            )

            summary_result = await session.execute(
                summary_query,
                {"validation_id": validation_id},
            )
            warning_count = summary_result.scalar_one()

            total_result = await session.execute(
                total_query,
                {
                    "from_datetime": from_datetime,
                    "geotab_database_id": geotab_database_id,
                    "idle_speed_threshold": IDLE_SPEED_THRESHOLD_KMH,
                },
            )
            total_count = total_result.scalar_one()

            validation.status = ValidationStatus.DONE
            validation.finished_at = datetime.utcnow()
            validation.warnings = warning_count
            validation.errors = 0
            validation.total = total_count

            logger.info(
                "Idle outlier validation %s completed for geotab_database_id=%s: warnings=%s",
                validation_id,
                geotab_database_id,
                warning_count,
            )

        await session.commit()


async def run_idle_outlier_validation_service(interval_seconds: int = 300) -> None:
    while True:
        try:
            await run_single_idle_outlier_validation()
        except Exception:
            logger.exception("Idle outlier validation run failed")

        await asyncio.sleep(interval_seconds)
