from fastapi import APIRouter, Depends, HTTPException
from modules.auth.dependencies.auth import get_current_user
from modules.geotab_database.schemas.geotab_database import (
    DatabaseEntryResponse,
    InitDatabaseRequest,
    InitDatabaseResponse,
)
from modules.geotab_database.dependencies.geotab_database import (
    init_database_impl,
    get_database_impl,
)

router = APIRouter(prefix="/database", tags=["database"])


@router.post("/", response_model=InitDatabaseResponse)
async def init_database(
    request: InitDatabaseRequest,
    current_user: dict = Depends(get_current_user),
) -> InitDatabaseResponse:
    """
    Initialize or update a Geotab database configuration.

    This endpoint stores the Geotab credentials and database information
    for the authenticated user. If an entry already exists for this email
    and database combination, it will be updated.
    """
    return await init_database_impl(request, current_user)


@router.get("/", response_model=DatabaseEntryResponse)
async def get_database(
    current_user: dict = Depends(get_current_user),
) -> DatabaseEntryResponse:
    """Retrieve the Geotab database configuration for the authenticated user."""

    return await get_database_impl(current_user)


@router.get("/get_session_id")
async def get_session_id(username: str, password: str, database: str) -> str:
    """
    Retrieve session information for the authenticated user.

    This endpoint can be used to verify that the user's session is active
    and to retrieve basic information about the user's authentication status.
    """

    import mygeotab

    # initialize the API client with the provided credentials
    client = mygeotab.API(
        username=username,
        password=password,
        database=database,
    )

    # authenticate the client to obtain the session id
    client.authenticate()

    # retrieve the session_id
    try:
        session_id = client.credentials.session_id
    except AttributeError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve session ID from Geotab client"
        )

    return session_id
