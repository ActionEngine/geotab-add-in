import logging
from fastapi import HTTPException
from modules.geotab_database.services.geotab_database import (
    add_or_replace_database,
    get_database_by_email_and_name,
)
from modules.geotab_database.schemas.geotab_database import (
    InitDatabaseRequest,
    InitDatabaseResponse,
    DatabaseEntryResponse,
)

logger = logging.getLogger(__name__)


async def init_database_impl(
    request: InitDatabaseRequest,
    current_user: dict,
) -> InitDatabaseResponse:
    """
    Initialize or update a Geotab database configuration.

    This endpoint stores the Geotab credentials and database information
    for the authenticated user. If an entry already exists for this email
    and database combination, it will be updated.
    """
    try:
        logger.info(
            f"Initializing database for user={request.user_name}, "
            f"database={request.database_name}"
        )

        db_entry = await add_or_replace_database(
            email=request.user_name,
            password=request.password,
            database=request.database_name,
        )

        return db_entry

    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise HTTPException(
            status_code=500, detail=f"Failed to initialize database: {str(e)}"
        )


async def get_database_impl(current_user: dict) -> DatabaseEntryResponse:
    """
    Get Geotab database configuration for the authenticated user.
    """

    email, database_name = current_user["email"], current_user["database"]

    logger.info(f"Fetching database for user={email}, database={database_name}")

    db_entry = await get_database_by_email_and_name(email, database_name)

    if not db_entry:
        raise HTTPException(
            status_code=404,
            detail=f"No database configuration found for user {email} and database {database_name}",
        )

    return DatabaseEntryResponse(
        email=db_entry.email,
        database_name=db_entry.database_name,
        ingestion_status=db_entry.ingestion_status.value,
        last_sync=db_entry.last_sync.isoformat() if db_entry.last_sync else None,
    )
