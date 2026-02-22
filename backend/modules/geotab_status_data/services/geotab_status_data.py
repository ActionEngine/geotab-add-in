import logging
from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
import mygeotab
from modules.geotab_status_data.models.geotab_status_data import GeotabStatusData

logger = logging.getLogger(__name__)


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
                "name": "Engine Speed",
                "unitOfMeasure": "rpm"
            },
            "version": "1.0.0"
        }
    
    Note:
        This function does not commit the session. The caller is responsible
        for committing the transaction, allowing for batch operations.
    """
    
    # Extract datetime
    status_datetime = status_data.get("dateTime")
    if isinstance(status_datetime, str):
        status_datetime = datetime.fromisoformat(status_datetime.replace("Z", "+00:00"))
    
    # Extract device information
    device = status_data.get("device", {})
    device_id = device.get("id", "")
    
    # Extract diagnostic information
    diagnostic = status_data.get("diagnostic", {})
    diagnostic_name = diagnostic.get("name", "")
    diagnostic_unit_of_measure = diagnostic.get("unitOfMeasure", "")
    
    # Extract data value
    data_value = status_data.get("data")
    if data_value is not None:
        try:
            data_value = float(data_value)
        except (ValueError, TypeError):
            logger.warning(f"Could not convert data value to float: {data_value}")
            data_value = None
    
    # Get external_id (StatusData id)
    external_id = status_data.get("id", "")
    
    # Get version
    version = status_data.get("version", "")
    
    # Create new status data entry
    status_entry = GeotabStatusData(
        datetime=status_datetime,
        device_id=device_id,
        external_id=external_id,
        data=data_value,
        diagnostic_name=diagnostic_name,
        diagnostic_unit_of_measure=diagnostic_unit_of_measure,
        version=version,
        geotab_database_id=geotab_database_id,
    )
    
    session.add(status_entry)
    
    return status_entry


async def get_status_data(
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
    Fetch StatusData from Geotab API with automatic pagination.
    
    Args:
        username: Geotab username/email
        password: Geotab password or session_id
        database: Geotab database name
        server: Geotab server (default: my.geotab.com)
        device_ids: Optional list of device IDs to filter by
        from_date: Optional start date for status data
        to_date: Optional end date for status data
        results_limit: Number of results per API call (default: 50000)
    
    Returns:
        List of all StatusData dictionaries from Geotab API
        
    Example usage:
        status_data = await get_status_data(
            username="user@example.com",
            password="password",
            database="database_name",
            device_ids=["b1234567890"],
            from_date=datetime(2026, 2, 1),
            to_date=datetime(2026, 2, 22)
        )
    """
    logger.info(
        f"Fetching StatusData from Geotab: database={database}, "
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
        
        # Fetch all StatusData with offset-based pagination
        all_records = []
        last_date = None
        last_id = None
        
        logger.info(f"Starting pagination with resultsLimit={results_limit}")
        
        while True:
            # Fetch batch of StatusData using offset pagination
            sort_params = {
                "sortBy": "date",
                "sortDirection": "asc",
            }
            if last_date is not None:
                sort_params["offset"] = last_date
            if last_id is not None:
                sort_params["lastId"] = last_id
            
            batch = api.get(
                "StatusData",
                search=search,
                resultsLimit=results_limit,
                sort=sort_params,
            )
            
            if not batch:
                logger.info(f"No more records at offset {last_date}")
                break
            
            all_records.extend(batch)
            logger.info(f"Fetched batch of {len(batch)} records (total: {len(all_records)})")
            
            # If we got fewer results than the limit, we've reached the end
            if len(batch) < results_limit:
                logger.info(f"Last batch returned {len(batch)} records, pagination complete")
                break
            
            # Update offset and lastId from the last record in the batch for next iteration
            last_record = batch[-1]
            last_date = last_record.get("dateTime")
            last_id = last_record.get("id")
        
        logger.info(f"Retrieved total of {len(all_records)} StatusData records from Geotab")
        
        return all_records
    
    except mygeotab.exceptions.AuthenticationException as e:
        logger.error(f"Geotab authentication failed: {e}")
        raise ValueError(f"Authentication failed: {str(e)}")
    except mygeotab.exceptions.MyGeotabException as e:
        logger.error(f"Geotab API error: {e}")
        raise ValueError(f"Geotab API error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error fetching StatusData: {e}")
        raise


async def get_feed_status_data(
    username: str,
    password: str,
    database: str,
    server: str = "my.geotab.com",
    feed_version: Optional[str] = None,
) -> tuple[List[dict], str]:
    """
    Fetch incremental StatusData using GetFeed from Geotab API.
    
    Args:
        username: Geotab username/email
        password: Geotab password or session_id
        database: Geotab database name
        server: Geotab server (default: my.geotab.com)
        feed_version: Optional feed version token from previous call
    
    Returns:
        Tuple of (List of StatusData dictionaries, new feed version token)
        
    Example usage:
        status_data, new_version = await get_feed_status_data(
            username="user@example.com",
            password="password",
            database="database_name",
            feed_version="abc123"
        )
    """
    logger.info(
        f"Fetching StatusData feed from Geotab: database={database}, "
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
            "typeName": "StatusData",
        }
        
        if feed_version:
            params["fromVersion"] = feed_version
        
        # Fetch StatusData using GetFeed
        result = api.call("GetFeed", **params)
        
        status_data = result.get("data", [])
        new_version = result.get("toVersion", "")
        
        logger.info(
            f"Retrieved {len(status_data)} new StatusData records from Geotab feed "
            f"(version: {new_version[:20] if new_version else 'none'})"
        )
        
        return status_data, new_version
    
    except mygeotab.exceptions.AuthenticationException as e:
        logger.error(f"Geotab authentication failed: {e}")
        raise ValueError(f"Authentication failed: {str(e)}")
    except mygeotab.exceptions.MyGeotabException as e:
        logger.error(f"Geotab API error: {e}")
        raise ValueError(f"Geotab API error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error fetching StatusData feed: {e}")
        raise
