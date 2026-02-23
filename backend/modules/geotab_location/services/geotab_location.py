import logging
from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
import mygeotab
from modules.geotab_location.models.geotab_location import GeotabLocation

logger = logging.getLogger(__name__)


def log_record_to_geotab_location(
    session: AsyncSession,
    log_record: dict,
    geotab_database_id: int,
) -> GeotabLocation:
    """
    Convert a Geotab LogRecord object to a GeotabLocation database entry.
    
    Args:
        session: SQLAlchemy AsyncSession for database operations
        log_record: Dictionary containing LogRecord data from Geotab API with:
            - dateTime: ISO format datetime string or datetime object
            - device: Device object with 'id' field
            - latitude: GPS latitude in decimal degrees
            - longitude: GPS longitude in decimal degrees
            - speed: Speed in km/h
        geotab_database_id: Foreign key reference to geotab_database table
    
    Returns:
        GeotabLocation: The created database entry (not yet committed)
        
    Example LogRecord structure:
        {
            "id": "a1234567890",
            "dateTime": "2026-02-22T10:30:00.000Z",
            "device": {"id": "b1234567890"},
            "latitude": 43.4643,
            "longitude": -79.6990,
            "speed": 50.5
        }
    
    Note:
        This function does not commit the session. The caller is responsible
        for committing the transaction, allowing for batch operations.
    """
    
    # Extract datetime
    log_datetime = log_record.get("dateTime")
    if isinstance(log_datetime, str):
        log_datetime = datetime.fromisoformat(log_datetime.replace("Z", "+00:00"))
    
    # Extract device information
    device = log_record.get("device", {})
    device_id = device.get("id", "")
    
    # Extract coordinates
    latitude = log_record.get("latitude")
    longitude = log_record.get("longitude")
    
    if latitude is None or longitude is None:
        raise ValueError(f"LogRecord missing required coordinates: lat={latitude}, lon={longitude}")
    
    # Create Point geometry (longitude, latitude order for WKT)
    point = Point(longitude, latitude)
    geometry = from_shape(point, srid=4326)
    
    # Extract speed (convert to integer if needed)
    speed = int(log_record.get("speed", 0))
    
    # Get external_id (LogRecord id)
    external_id = log_record.get("id", "")
    
    # Create new location entry
    location_entry = GeotabLocation(
        datetime=log_datetime,
        device_id=device_id,
        external_id=external_id,
        geometry=geometry,
        speed=speed,
        geotab_database_id=geotab_database_id,
    )
    
    session.add(location_entry)
    
    return location_entry


async def get_log_records(
    username: str,
    password: str,
    database: str,
    server: str = "my.geotab.com",
    device_ids: Optional[List[str]] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    results_limit: int = 50000,
) -> List[dict]:
    """
    Fetch LogRecords from Geotab API with automatic pagination.
    
    Args:
        username: Geotab username/email
        password: Geotab password or session_id
        database: Geotab database name
        server: Geotab server (default: my.geotab.com)
        device_ids: Optional list of device IDs to filter by
        from_date: Optional start date for log records
        to_date: Optional end date for log records
        results_limit: Number of results per API call (default: 50000)
    
    Returns:
        List of all LogRecord dictionaries from Geotab API
        
    Example usage:
        log_records = await get_log_records(
            username="user@example.com",
            password="password",
            database="database_name",
            device_ids=["b1234567890"],
            from_date=datetime(2026, 2, 1),
            to_date=datetime(2026, 2, 22)
        )
    """
    logger.info(
        f"Fetching LogRecords from Geotab: database={database}, "
        f"devices={len(device_ids) if device_ids else 'all'}, "
        f"from_date={from_date}, to_date={to_date}"
    )
    
    try:
        # Create Geotab API instance
        api = mygeotab.API(
            username=username,
            password=password,
            database=database,
            server=server,
        )
        
        # Authenticate
        api.authenticate()
        
        # Build search criteria
        search = {}
        
        if device_ids:
            # Filter by specific devices
            search["deviceSearch"] = {"id": device_ids[0] if len(device_ids) == 1 else device_ids}
        
        if from_date:
            search["fromDate"] = from_date.isoformat()
        
        if to_date:
            search["toDate"] = to_date.isoformat()
        
        # Fetch all LogRecords with offset-based pagination
        all_records = []
        offset = 0
        
        logger.info(f"Starting pagination with resultsLimit={results_limit}")
        
        while True:
            # Fetch batch of LogRecords using offset pagination
            batch = api.get(
                "LogRecord",
                search=search,
                resultsLimit=results_limit,
                offset=offset
            )
            
            if not batch:
                logger.info(f"No more records at offset {offset}")
                break
            
            all_records.extend(batch)
            logger.info(f"Fetched batch of {len(batch)} records at offset {offset} (total: {len(all_records)})")
            
            # If we got fewer results than the limit, we've reached the end
            if len(batch) < results_limit:
                logger.info(f"Last batch returned {len(batch)} records, pagination complete")
                break
            
            # Move to next page
            offset += results_limit
        
        logger.info(f"Retrieved total of {len(all_records)} LogRecords from Geotab")
        
        return all_records
    
    except mygeotab.exceptions.AuthenticationException as e:
        logger.error(f"Geotab authentication failed: {e}")
        raise ValueError(f"Authentication failed: {str(e)}")
    except mygeotab.exceptions.MyGeotabException as e:
        logger.error(f"Geotab API error: {e}")
        raise ValueError(f"Geotab API error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error fetching LogRecords: {e}")
        raise


async def get_feed_log_records(
    username: str,
    password: str,
    database: str,
    server: str = "my.geotab.com",
    feed_version: Optional[str] = None,
) -> tuple[List[dict], str]:
    """
    Fetch incremental LogRecords using GetFeed from Geotab API.
    
    Args:
        username: Geotab username/email
        password: Geotab password or session_id
        database: Geotab database name
        server: Geotab server (default: my.geotab.com)
        feed_version: Optional feed version token from previous call
    
    Returns:
        Tuple of (List of LogRecord dictionaries, new feed version token)
        
    Example usage:
        log_records, new_version = await get_feed_log_records(
            username="user@example.com",
            password="password",
            database="database_name",
            feed_version="abc123"
        )
    """
    logger.info(
        f"Fetching LogRecords feed from Geotab: database={database}, "
        f"feed_version={'initial' if not feed_version else feed_version[:20]}"
    )
    
    try:
        # Create Geotab API instance
        api = mygeotab.API(
            username=username,
            password=password,
            database=database,
            server=server,
        )
        
        # Authenticate
        api.authenticate()
        
        # Build GetFeed parameters
        params = {
            "typeName": "LogRecord",
        }
        
        if feed_version:
            params["fromVersion"] = feed_version
        
        # Fetch LogRecords using GetFeed
        result = api.call("GetFeed", **params)
        
        log_records = result.get("data", [])
        new_version = result.get("toVersion", "")
        
        logger.info(
            f"Retrieved {len(log_records)} new LogRecords from Geotab feed "
            f"(version: {new_version[:20] if new_version else 'none'})"
        )
        
        return log_records, new_version
    
    except mygeotab.exceptions.AuthenticationException as e:
        logger.error(f"Geotab authentication failed: {e}")
        raise ValueError(f"Authentication failed: {str(e)}")
    except mygeotab.exceptions.MyGeotabException as e:
        logger.error(f"Geotab API error: {e}")
        raise ValueError(f"Geotab API error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error fetching LogRecords feed: {e}")
        raise
