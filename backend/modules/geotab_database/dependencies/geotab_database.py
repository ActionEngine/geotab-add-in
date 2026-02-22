import logging
from fastapi import HTTPException
from modules.geotab_database.services.geotab_database import add_or_replace_database
from modules.geotab_database.schemas.geotab_database import (
    InitDatabaseRequest,
    InitDatabaseResponse,
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
