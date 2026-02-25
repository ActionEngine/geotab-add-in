import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from modules.auth.dependencies.auth import get_current_user
from modules.geotab_database.services.geotab_database import (
    get_database_by_email_and_name,
)
from modules.geotab_location.services.mvt_service import (
    generate_mvt_tile,
    generate_teleportation_mvt_tile,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tiles", tags=["location"])


@router.get(
    "/",
    responses={
        200: {
            "content": {"application/vnd.mapbox-vector-tile": {}},
            "description": "Returns a Mapbox Vector Tile (binary data)",
        }
    },
)
async def get_mvt_tile(
    z: int,
    x: int,
    y: int,
    date_from: datetime | None = Query(None, description="Filter from this date"),
    date_to: datetime | None = Query(None, description="Filter to this date"),
    current_user: dict = Depends(get_current_user),
) -> Response:
    """
    Generate Mapbox Vector Tile (MVT) for Geotab location data.

    Args:
        z: Zoom level (0-22)
        x: Tile X coordinate
        y: Tile Y coordinate
        date_from: Optional start date filter (ISO format)
        date_to: Optional end date filter (ISO format)

    Returns:
        MVT tile as application/vnd.mapbox-vector-tile
    """

    # Validate tile coordinates
    if z < 0 or z > 22:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid zoom level: {z}. Must be between 0 and 22",
        )

    max_tile = 2**z
    if x < 0 or x >= max_tile:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid tile X coordinate: {x}. Must be between 0 and {max_tile - 1} for zoom {z}",
        )

    if y < 0 or y >= max_tile:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid tile Y coordinate: {y}. Must be between 0 and {max_tile - 1} for zoom {z}",
        )

    email, database_name = current_user["email"], current_user["database"]

    logger.info(
        f"Generating MVT tile z={z}, x={x}, y={y} for user={email}, "
        f"database={database_name}, date_from={date_from}, date_to={date_to}"
    )

    # Get database entry to get geotab_database_id
    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        raise HTTPException(
            status_code=404,
            detail=f"No database configuration found for user {email} and database {database_name}",
        )

    # Generate MVT tile
    tile_data = await generate_mvt_tile(
        geotab_database_id=db_entry.id,
        z=z,
        x=x,
        y=y,
        date_from=date_from,
        date_to=date_to,
    )

    logger.info(
        f"Returning MVT tile: {len(tile_data)} bytes for "
        f"z={z}, x={x}, y={y}, user={email}"
    )

    return Response(
        content=tile_data,
        media_type="application/vnd.mapbox-vector-tile",
        headers={
            "Cache-Control": "public, max-age=3600",
            "Access-Control-Allow-Origin": "*",
        },
    )


@router.get(
    "/teleportation",
    responses={
        200: {
            "content": {"application/vnd.mapbox-vector-tile": {}},
            "description": "MVT tile with trajectory lines and teleportation flag points",
        }
    },
)
async def get_teleportation_mvt_tile(
    z: int,
    x: int,
    y: int,
    date_from: datetime | None = Query(None, description="Filter from this date"),
    date_to: datetime | None = Query(None, description="Filter to this date"),
    current_user: dict = Depends(get_current_user),
) -> Response:
    """
    MVT tile for teleportation validation visualization.
    Returns two layers:
      - 'trajectory'          : LINESTRING segments between consecutive GPS points per device
      - 'teleportation_flags' : points exceeding the speed threshold (with implied_speed_kmh)
    """

    if z < 0 or z > 22:
        raise HTTPException(status_code=400, detail=f"Invalid zoom level: {z}")
    max_tile = 2**z
    if not (0 <= x < max_tile):
        raise HTTPException(status_code=400, detail=f"Invalid tile X: {x}")
    if not (0 <= y < max_tile):
        raise HTTPException(status_code=400, detail=f"Invalid tile Y: {y}")

    email, database_name = current_user["email"], current_user["database"]
    db_entry = await get_database_by_email_and_name(email, database_name)
    if not db_entry:
        raise HTTPException(
            status_code=404,
            detail=f"No database configuration found for user {email} and database {database_name}",
        )

    tile_data = await generate_teleportation_mvt_tile(
        geotab_database_id=db_entry.id,
        z=z,
        x=x,
        y=y,
        date_from=date_from,
        date_to=date_to,
    )

    return Response(
        content=tile_data,
        media_type="application/vnd.mapbox-vector-tile",
        headers={
            "Cache-Control": "no-cache",
            "Access-Control-Allow-Origin": "*",
        },
    )
