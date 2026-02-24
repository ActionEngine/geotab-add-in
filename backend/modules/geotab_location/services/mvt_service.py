import logging
from datetime import datetime
from sqlalchemy import text
from database.database import SessionLocal
import math

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
