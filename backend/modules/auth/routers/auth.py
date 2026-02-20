from fastapi import APIRouter, Response

from modules.auth.dependencies.auth import (
    verify_geotab_token,
    authenticate_geotab_credentials,
    set_auth_cookie,
)
from modules.auth.schemas.auth import (
    GeotabAuthRequest,
    GeotabCredentialsRequest,
    TokenResponse,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/geotab", response_model=TokenResponse)
async def geotab_auth(data: GeotabAuthRequest, response: Response):
    """Authenticate with Geotab OAuth token"""

    result = await verify_geotab_token(data.geotab_token)
    set_auth_cookie(response, result["access_token"])

    return result


@router.post("/geotab/credentials", response_model=TokenResponse)
async def geotab_credentials_auth(data: GeotabCredentialsRequest, response: Response):
    """Authenticate with Geotab username/password"""

    result = await authenticate_geotab_credentials(
        data.username, data.password, data.database
    )
    set_auth_cookie(response, result["access_token"])

    return result
