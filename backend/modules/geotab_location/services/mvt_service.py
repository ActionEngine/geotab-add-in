from datetime import datetime
import logging
import math
from sqlalchemy import text
from database.database import SessionLocal

logger = logging.getLogger(__name__)


def tile_to_bbox(z: int, x: int, y: int) -> tuple:
    """Convert tile coordinates to bounding box in Web Mercator (EPSG:3857)."""

    def num2deg(xtile, ytile, zoom):
        n = 2.0**zoom
        lon_deg = xtile / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
        lat_deg = math.degrees(lat_rad)
        return (lon_deg, lat_deg)

    # Convert to Web Mercator
    def lonlat_to_webmercator(lon, lat):
        x = lon * 20037508.34 / 180.0
        y = math.log(math.tan((90 + lat) * math.pi / 360.0)) / (math.pi / 180.0)
        y = y * 20037508.34 / 180.0
        return (x, y)

    # Get corners of the tile
    nw = num2deg(x, y, z)
    se = num2deg(x + 1, y + 1, z)

    min_lon, max_lat = nw
    max_lon, min_lat = se

    min_x, max_y = lonlat_to_webmercator(min_lon, max_lat)
    max_x, min_y = lonlat_to_webmercator(max_lon, min_lat)

    return (min_x, min_y, max_x, max_y)


async def generate_mvt_tile(
    geotab_database_id: int,
    z: int,
    x: int,
    y: int,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
) -> bytes:
    """
    Generate MVT tile for geotab locations.

    Args:
        geotab_database_id: ID of the geotab database
        z: Zoom level
        x: Tile X coordinate
        y: Tile Y coordinate
        date_from: Filter locations from this date (optional)
        date_to: Filter locations to this date (optional)

    Returns:
        MVT tile as bytes
    """

    logger.info(
        f"Generating MVT tile: z={z}, x={x}, y={y}, "
        f"geotab_database_id={geotab_database_id}, "
        f"date_from={date_from}, date_to={date_to}"
    )

    bbox = tile_to_bbox(z, x, y)
    logger.debug(f"Tile bbox (Web Mercator): {bbox}")

    # Build WHERE conditions based on date filters
    date_conditions = []
    params = {
        "db_id": geotab_database_id,
        "minx": bbox[0],
        "miny": bbox[1],
        "maxx": bbox[2],
        "maxy": bbox[3],
    }

    if date_from is not None:
        date_conditions.append("AND datetime >= :date_from")
        params["date_from"] = date_from

    if date_to is not None:
        date_conditions.append("AND datetime <= :date_to")
        params["date_to"] = date_to

    date_filter = " ".join(date_conditions)

    # Build SQL query for MVT generation
    query = text(
        f"""
        WITH mvtgeom AS (
            SELECT
                ST_AsMVTGeom(
                    ST_Transform(geometry, 3857),
                    ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857),
                    4096,
                    256,
                    true
                ) AS geom,
                id,
                device_id,
                external_id,
                datetime,
                speed
            FROM geotab_location
            WHERE geotab_database_id = :db_id
                AND geometry IS NOT NULL
                AND ST_Transform(geometry, 3857) && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
                {date_filter}
        )
        SELECT ST_AsMVT(mvtgeom.*, 'geotab_locations', 4096, 'geom')
        FROM mvtgeom
        WHERE geom IS NOT NULL;
        """
    )

    async with SessionLocal() as session:
        # First, check if there's any data in the bbox
        count_query = text(
            f"""
            SELECT COUNT(*) 
            FROM geotab_location
            WHERE geotab_database_id = :db_id
                AND geometry IS NOT NULL
                AND ST_Transform(geometry, 3857) && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
                {date_filter}
            """
        )
        count_result = await session.execute(count_query, params)
        row_count = count_result.scalar()

        logger.info(
            f"Found {row_count} location records in bbox for "
            f"geotab_database_id={geotab_database_id}, z={z}, x={x}, y={y}"
        )

        if row_count == 0:
            logger.warning(
                f"No data in bbox for geotab_database_id={geotab_database_id}, "
                f"z={z}, x={x}, y={y}, bbox={bbox}"
            )
            return b""

        # Generate MVT
        result = await session.execute(query, params)
        tile = result.scalar()

        if tile is None or tile == b"":
            logger.warning(
                f"ST_AsMVT returned empty result despite {row_count} rows present"
            )
            return b""

        tile_bytes = bytes(tile)

        logger.info(
            f"Generated MVT tile: {len(tile_bytes)} bytes for "
            f"geotab_database_id={geotab_database_id}, z={z}, x={x}, y={y}"
        )

        return tile_bytes


async def generate_teleportation_mvt_tile(
    geotab_database_id: int,
    z: int,
    x: int,
    y: int,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
) -> bytes:
    """
    Generate MVT tile with two layers for teleportation validation:
      - 'trajectory'          : LINESTRING segments between consecutive points per device
      - 'teleportation_flags' : points flagged as teleportation with implied_speed_kmh
    """

    bbox = tile_to_bbox(z, x, y)
    params: dict = {
        "db_id": geotab_database_id,
        "minx": bbox[0],
        "miny": bbox[1],
        "maxx": bbox[2],
        "maxy": bbox[3],
    }

    date_conditions = []
    if date_from is not None:
        date_conditions.append("AND gl.datetime >= :date_from")
        params["date_from"] = date_from
    if date_to is not None:
        date_conditions.append("AND gl.datetime <= :date_to")
        params["date_to"] = date_to

    date_filter = " ".join(date_conditions)

    # Two layers concatenated as bytea — PostGIS supports || for MVT
    query = text(
        f"""
        WITH ordered AS (
            SELECT
                id,
                device_id,
                datetime,
                geometry,
                LAG(geometry) OVER (PARTITION BY device_id ORDER BY datetime) AS prev_geometry,
                LAG(id)       OVER (PARTITION BY device_id ORDER BY datetime) AS prev_id
            FROM geotab_location gl
            WHERE geotab_database_id = :db_id
              AND geometry IS NOT NULL
              {date_filter}
        ),
        segments AS (
            SELECT
                device_id,
                id AS to_location_id,
                prev_id AS from_location_id,
                ST_MakeLine(prev_geometry, geometry) AS geom
            FROM ordered
            WHERE prev_geometry IS NOT NULL
        ),
        latest_validation AS (
            SELECT id AS validation_id
            FROM validation
            WHERE validation_type = 'TELEPORTATION'
              AND geotab_database_id = :db_id
            ORDER BY started_at DESC
            LIMIT 1
        ),
        flagged AS (
            SELECT
                gl.id,
                gl.device_id,
                gl.datetime,
                gl.geometry,
                tr.implied_speed_kmh
            FROM teleportation_results tr
            JOIN latest_validation lv ON tr.validation_id = lv.validation_id
            JOIN geotab_location gl ON gl.id = tr.geotab_location_id
        ),
        -- Layer 1: trajectory segments that intersect the tile
        traj_mvt AS (
            SELECT ST_AsMVTGeom(
                ST_Transform(geom, 3857),
                ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857),
                4096, 256, true
            ) AS geom,
            device_id,
            from_location_id,
            to_location_id
            FROM segments
            WHERE ST_Transform(geom, 3857) && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
        ),
        -- Layer 2: flagged teleportation points that intersect the tile
        flags_mvt AS (
            SELECT ST_AsMVTGeom(
                ST_Transform(geometry, 3857),
                ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857),
                4096, 256, true
            ) AS geom,
            id,
            device_id,
            datetime,
            implied_speed_kmh
            FROM flagged
            WHERE ST_Transform(geometry, 3857) && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
        )
        SELECT
            (
                SELECT COALESCE(ST_AsMVT(traj_mvt.*, 'trajectory',       4096, 'geom'), ''::bytea) FROM traj_mvt  WHERE geom IS NOT NULL
            )
            ||
            (
                SELECT COALESCE(ST_AsMVT(flags_mvt.*, 'teleportation_flags', 4096, 'geom'), ''::bytea) FROM flags_mvt WHERE geom IS NOT NULL
            );
        """
    )

    async with SessionLocal() as session:
        result = await session.execute(query, params)
        tile = result.scalar()

    if tile is None:
        return b""

    return bytes(tile)


async def generate_idle_outlier_mvt_tile(
    geotab_database_id: int,
    z: int,
    x: int,
    y: int,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
) -> bytes:
    """
    Generate MVT tile with three layers for idle-outlier validation:
      - 'idle_clusters'       : convex-hull polygons of DBSCAN clusters (pre-computed,
                                stored in idle_clusters table — no per-request DBSCAN)
      - 'idle_normal'         : recent idle points that fall within a known cluster (normal)
      - 'idle_outlier_flags'  : recent idle points flagged as outliers (outside all clusters)
    """
    bbox = tile_to_bbox(z, x, y)
    params: dict = {
        "db_id": geotab_database_id,
        "minx": bbox[0],
        "miny": bbox[1],
        "maxx": bbox[2],
        "maxy": bbox[3],
    }

    date_conditions = []
    if date_from is not None:
        date_conditions.append("AND gl.datetime >= :date_from")
        params["date_from"] = date_from
    if date_to is not None:
        date_conditions.append("AND gl.datetime <= :date_to")
        params["date_to"] = date_to
    date_filter = " ".join(date_conditions)

    query = text(
        f"""
        WITH latest_validation AS (
            SELECT id AS validation_id
            FROM validation
            WHERE validation_type = 'IDLE_OUTLIER'
              AND geotab_database_id = :db_id
            ORDER BY started_at DESC
            LIMIT 1
        ),
        -- Layer 1: precomputed cluster polygons (cheap table scan)
        clusters_mvt AS (
            SELECT
                ST_AsMVTGeom(
                    ST_Transform(geometry, 3857),
                    ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857),
                    4096, 256, true
                ) AS geom,
                cluster_id,
                point_count
            FROM idle_clusters
            WHERE geotab_database_id = :db_id
              AND ST_Transform(geometry, 3857)
                  && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
        ),
        -- Layer 2: normal idle points (in a known cluster, not flagged as outlier)
        -- Identified by LEFT JOIN exclusion: recent idle points absent from idle_outlier_results
        normal_mvt AS (
            SELECT
                ST_AsMVTGeom(
                    ST_Transform(gl.geometry, 3857),
                    ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857),
                    4096, 256, true
                ) AS geom,
                gl.id,
                gl.device_id,
                gl.datetime,
                gl.speed
            FROM geotab_location gl
            JOIN latest_validation lv ON true
            LEFT JOIN idle_outlier_results ior
                   ON ior.geotab_location_id = gl.id
                  AND ior.validation_id = lv.validation_id
            WHERE gl.geotab_database_id = :db_id
              AND gl.geometry IS NOT NULL
              AND gl.speed <= 5
              AND ior.geotab_location_id IS NULL
              AND ST_Transform(gl.geometry, 3857)
                  && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
              {date_filter}
        ),
        -- Layer 3: flagged idle outlier points
        flags_mvt AS (
            SELECT
                ST_AsMVTGeom(
                    ST_Transform(gl.geometry, 3857),
                    ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857),
                    4096, 256, true
                ) AS geom,
                gl.id,
                gl.device_id,
                gl.datetime,
                gl.speed
            FROM idle_outlier_results ior
            JOIN latest_validation lv ON ior.validation_id = lv.validation_id
            JOIN geotab_location gl ON gl.id = ior.geotab_location_id
            WHERE ST_Transform(gl.geometry, 3857)
                  && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
              {date_filter}
        )
        SELECT
            (
                SELECT COALESCE(ST_AsMVT(clusters_mvt.*, 'idle_clusters',      4096, 'geom'), ''::bytea)
                FROM clusters_mvt WHERE geom IS NOT NULL
            )
            ||
            (
                SELECT COALESCE(ST_AsMVT(normal_mvt.*,   'idle_normal',        4096, 'geom'), ''::bytea)
                FROM normal_mvt WHERE geom IS NOT NULL
            )
            ||
            (
                SELECT COALESCE(ST_AsMVT(flags_mvt.*,    'idle_outlier_flags', 4096, 'geom'), ''::bytea)
                FROM flags_mvt WHERE geom IS NOT NULL
            );
        """
    )

    async with SessionLocal() as session:
        result = await session.execute(query, params)
        tile = result.scalar()

    if tile is None:
        return b""

    return bytes(tile)


async def generate_segments_mvt_tile(
    geotab_database_id: int,
    z: int,
    x: int,
    y: int,
) -> bytes:
    """
    Generate MVT tile for Overture road segments stored in overture_segments.

    Args:
        geotab_database_id: ID of the geotab database
        z: Zoom level
        x: Tile X coordinate
        y: Tile Y coordinate

    Returns:
        MVT tile as bytes (empty bytes if no data in tile)
    """

    logger.info(
        f"Generating segments MVT tile: z={z}, x={x}, y={y}, "
        f"geotab_database_id={geotab_database_id}"
    )

    bbox = tile_to_bbox(z, x, y)
    logger.debug(f"Tile bbox (Web Mercator): {bbox}")

    params = {
        "db_id": geotab_database_id,
        "minx": bbox[0],
        "miny": bbox[1],
        "maxx": bbox[2],
        "maxy": bbox[3],
    }

    query = text(
        """
        WITH mvtgeom AS (
            SELECT
                ST_AsMVTGeom(
                    ST_Transform(geometry, 3857),
                    ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857),
                    4096,
                    256,
                    true
                ) AS geom,
                id,
                external_id,
                names,
                class_code,
                subtype,
                road_surface,
                speed_limits
            FROM overture_segments
            WHERE geotab_database_id = :db_id
                AND geometry IS NOT NULL
                AND ST_Transform(geometry, 3857) && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
        )
        SELECT ST_AsMVT(mvtgeom.*, 'overture_segments', 4096, 'geom')
        FROM mvtgeom
        WHERE geom IS NOT NULL;
        """
    )

    async with SessionLocal() as session:
        count_query = text(
            """
            SELECT COUNT(*)
            FROM overture_segments
            WHERE geotab_database_id = :db_id
                AND geometry IS NOT NULL
                AND ST_Transform(geometry, 3857) && ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 3857)
            """
        )
        count_result = await session.execute(count_query, params)
        row_count = count_result.scalar()

        logger.info(
            f"Found {row_count} segment records in bbox for "
            f"geotab_database_id={geotab_database_id}, z={z}, x={x}, y={y}"
        )

        if row_count == 0:
            return b""

        result = await session.execute(query, params)
        tile = result.scalar()

        if tile is None or tile == b"":
            logger.warning(
                f"ST_AsMVT returned empty result despite {row_count} rows present"
            )
            return b""

        tile_bytes = bytes(tile)

        logger.info(
            f"Generated segments MVT tile: {len(tile_bytes)} bytes for "
            f"geotab_database_id={geotab_database_id}, z={z}, x={x}, y={y}"
        )

        return tile_bytes
