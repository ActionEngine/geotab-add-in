from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
import mygeotab
from logging_config import configure_logger
from modules.geotab_status_data.models.geotab_status_data import GeotabStatusData

logger = configure_logger(__name__)


def status_data_to_geotab_status_data(
    session: AsyncSession,
    status_data: dict,
    geotab_database_id: int,
) -> GeotabStatusData:
    """
    Convert a Geotab StatusData object to a GeotabStatusData database entry.
    
    Args:
        session: SQLAlchemy AsyncSession for database operations
        status_data: Dictionary containing StatusData from Geotab API with:
            - dateTime: ISO format datetime string or datetime object
            - device: Device object with 'id' field
            - data: The numeric value of the status data
            - diagnostic: Diagnostic object with 'name' and optionally 'unitOfMeasure'
            - version: Optional version string
        geotab_database_id: Foreign key reference to geotab_database table
    
    Returns:
        GeotabStatusData: The created database entry (not yet committed)
        
    Example StatusData structure:
        {
            "id": "a1234567890",
            "dateTime": "2026-02-22T10:30:00.000Z",
            "device": {"id": "b1234567890"},
            "data": 98.5,
            "diagnostic": {
                "id": "DiagnosticEngineSpeedId",
            },
            "version": "1.0.0"
        }
    
    Note:
        This function does not commit the session. The caller is responsible
        for committing the transaction, allowing for batch operations.
    """
    
    status_datetime: datetime = status_data["dateTime"]

    device = status_data["device"]
    device_id = device["id"]

    diagnostic = status_data["diagnostic"]
    diagnostic_id = diagnostic["id"]

    data_value = float(status_data["data"])

    external_id = status_data["id"]
    version = status_data["version"]

    status_entry = GeotabStatusData(
        datetime=status_datetime,
        device_id=device_id,
        external_id=external_id,
        data=data_value,
        diagnostic_id=diagnostic_id,
        version=version,
        geotab_database_id=geotab_database_id,
    )

    session.add(status_entry)

    return status_entry


async def get_feed_status_data(
    api,
    feed_version: Optional[str] = None,
) -> tuple[list[dict], str]:
    """
    Fetch incremental StatusData using GetFeed from Geotab API.
    
    Args:
        api: mygeotab.API instance
        feed_version: Optional feed version token from previous call
    
    Returns:
        Tuple of (List of StatusData dictionaries, new feed version token)
        
    Example usage:
        status_data, new_version = await get_feed_status_data(
            api=mygeotab.API(
                username="user@example.com",
                password="password",
                database="database_name"
            ),
            feed_version="abc123"
        )
    """
    logger.info(
        f"Fetching StatusData feed from Geotab: database={api.credentials.database}, "
        f"feed_version={'initial' if not feed_version else feed_version[:20]}"
    )
    # Build GetFeed parameters
    params = {
        "typeName": "StatusData",
    }
    if feed_version:
        params["fromVersion"] = feed_version
    # Fetch StatusData using GetFeed
    result = api.call("GetFeed", **params)
    status_data = result.get("data", [])
    new_version = result["toVersion"]
    logger.info(
        f"Retrieved {len(status_data)} new StatusData records from Geotab feed "
        f"(version: {new_version[:20] if new_version else 'none'})"
    )
    return status_data, new_version
