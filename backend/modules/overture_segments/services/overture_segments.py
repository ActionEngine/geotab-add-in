import json
from typing import Optional
from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2.shape import from_shape
from shapely.geometry import box, shape
from shapely import wkb
from shapely.wkt import loads as wkt_loads
import duckdb
from logging_config import configure_logger

from modules.overture_segments.models.overture_segments import OvertureSegments
from modules.geotab_location.models.geotab_location import GeotabLocation
from database.database import SessionLocal

logger = configure_logger(__name__)


async def calculate_points_envelope(geotab_database_id: int) -> Optional[tuple]:
    """
    Calculate the bounding box (envelope) of all ingested location points
    for a given geotab_database.

    Args:
        geotab_database_id: ID of the geotab_database entry

    Returns:
        Tuple of (minx, miny, maxx, maxy) or None if no points exist
    """
    logger.info(f"Calculating envelope for database_id={geotab_database_id}")

    try:
        async with SessionLocal() as session:
            # Query the bounding box of all points for the given database
            result = await session.execute(
                select(
                    func.ST_XMin(func.ST_Extent(GeotabLocation.geometry)).label("minx"),
                    func.ST_YMin(func.ST_Extent(GeotabLocation.geometry)).label("miny"),
                    func.ST_XMax(func.ST_Extent(GeotabLocation.geometry)).label("maxx"),
                    func.ST_YMax(func.ST_Extent(GeotabLocation.geometry)).label("maxy"),
                ).where(GeotabLocation.geotab_database_id == geotab_database_id)
            )

            row = result.first()

            if row and all(v is not None for v in row):
                envelope = tuple(float(v) for v in row)
                logger.info(f"Calculated envelope: {envelope}")
                return envelope
            else:
                logger.warning(
                    f"No valid location points found for database_id={geotab_database_id}"
                )
                return None

    except Exception as e:
        logger.error(f"Error calculating envelope: {e}")
        raise


def get_overture_segments_from_duckdb(
    bbox: tuple, release_tag: str = "2026-02-18.0"
) -> list:
    """
    Query Overture Maps data for road segments within a bounding box using DuckDB.

    Args:
        bbox: Tuple of (minx, miny, maxx, maxy) bounding box coordinates
        release_tag: Overture release tag (default: "latest")

    Returns:
        List of segment objects with geometry and properties
    """
    logger.info(f"Querying Overture segments for bbox={bbox}, release={release_tag}")

    minx, miny, maxx, maxy = bbox
    try:
        # Initialize DuckDB connection
        conn = duckdb.connect(":memory:")

        # Install and load required extensions
        conn.install_extension("httpfs")
        conn.load_extension("httpfs")
        conn.install_extension("json")
        conn.load_extension("json")
        conn.execute("SET s3_region='us-west-2'")

        # Query Overture segments from S3 with spatial filtering
        # Using Overture Data segments with bbox filter
        query = f"""
        SELECT
            id,
            names,
            class,
            subclass,
            road_surface,
            speed_limits,
            geometry,
            bbox
        FROM read_parquet(
            's3://overturemaps-us-west-2/release/{release_tag}/theme=transportation/type=segment/*',
            hive_partitioning=1,
            filename=true
        )
        WHERE
            bbox.xmin <= {maxx}
            AND bbox.xmax >= {minx}
            AND bbox.ymin <= {maxy}
            AND bbox.ymax >= {miny}
        """

        # Execute query on DuckDB
        result = conn.execute(query).fetchall()

        # Get column information
        columns = [desc[0] for desc in conn.description]

        # Convert results to list of dictionaries
        segments = []
        for row in result:
            segment = dict(zip(columns, row))
            segments.append(segment)

        conn.close()

        logger.info(f"Retrieved {len(segments)} segments from Overture")
        return segments

    except Exception as e:
        logger.error(f"Error querying Overture segments: {e}")
        raise


async def save_overture_segment(
    session: AsyncSession,
    segment: dict,
    geotab_database_id: int,
) -> OvertureSegments:
    """
    Convert an Overture segment object to a database entry and save it.

    Args:
        session: SQLAlchemy AsyncSession for database operations
        segment: Dictionary containing segment data from Overture Maps API with:
            - id: Unique segment identifier
            - names: Array of name objects
            - classes: Array of class codes
            - subclasses: Array of subclass codes
            - road_surface: Road surface type
            - road_status: Road status
            - speed_limits: Array of speed limit objects
            - geometry: GeoJSON geometry
        geotab_database_id: Foreign key reference to geotab_database table

    Returns:
        OvertureSegments: The created database entry (not yet committed)
    """

    try:
        geometry_value = segment.get("geometry")
        geom = wkb.loads(bytes(geometry_value))
        geometry = from_shape(geom, srid=4326)
        bbox = segment.get("bbox", None)
        names = segment.get("names", None)
        class_code = segment.get("class", None)
        subtype = segment.get("subclass", None)
        road_surface = segment.get("road_surface")
        speed_limits = segment.get("speed_limits", None)

        # Create segment entry
        segment_entry = OvertureSegments(
            external_id=segment.get("id", ""),
            geometry=geometry,
            bbox=bbox,
            geotab_database_id=geotab_database_id,
            names=names if names else None,
            class_code=class_code,
            subtype=subtype,
            road_surface=road_surface,
            speed_limits=speed_limits,
        )

        session.add(segment_entry)
        return segment_entry

    except Exception as e:
        logger.error(f"Error saving segment {segment.get('id')}: {e}")
        raise


async def ingest_overture_segments(
    geotab_database_id: int,
    release_tag: str = "2026-02-18.0",
) -> None:
    """
    Ingest Overture Map segments within the envelope of ingested Geotab locations.

    This function:
    1. Calculates the bounding box of all ingested location points
    2. Queries Overture Maps for road segments within that area
    3. Saves segments to the overture_segments table

    Args:
        geotab_database_id: ID of the geotab_database entry
        release_tag: Overture release to query (default: "latest")
    """
    logger.info(
        f"Starting Overture segments ingestion for database_id={geotab_database_id}, "
        f"release={release_tag}"
    )

    try:
        # Step 1: Calculate envelope of ingested points
        envelope = await calculate_points_envelope(geotab_database_id)

        if not envelope:
            logger.warning(
                f"No location points found for database_id={geotab_database_id}, "
                "skipping segment ingestion"
            )
            return

        # Step 2: Query Overture segments from DuckDB
        segments = get_overture_segments_from_duckdb(
            bbox=envelope, release_tag=release_tag
        )

        if not segments:
            logger.info(f"No segments found within bbox {envelope}")
            return

        # Step 3: Save segments to database in batches
        batch_size = 1000
        total_saved = 0

        logger.info(f"Saving {len(segments)} segments to database...")

        async with SessionLocal() as session:
            for i, segment in enumerate(segments):
                try:
                    await save_overture_segment(
                        session=session,
                        segment=segment,
                        geotab_database_id=geotab_database_id,
                    )

                    # Commit in batches
                    if (i + 1) % batch_size == 0:
                        await session.commit()
                        total_saved += batch_size
                        logger.info(f"Saved {total_saved} segments...")

                except Exception as e:
                    logger.warning(f"Failed to save segment {segment.get('id')}: {e}")
                    continue

            # Commit remaining segments
            await session.commit()
            total_saved = len(segments)

        logger.info(
            f"Successfully ingested {total_saved} overture segments "
            f"for database_id={geotab_database_id}"
        )

    except Exception as e:
        logger.error(f"Error during overture segments ingestion: {e}")
        raise
