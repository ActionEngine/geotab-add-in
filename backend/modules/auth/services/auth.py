import os
import logging
from jose import jwt
from dotenv import load_dotenv
from fastapi import HTTPException
import mygeotab

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "supersecret")
JWT_ALGORITHM = "HS256"

logger = logging.getLogger(__name__)


def create_access_token(data: dict) -> str:
    """Create a JWT access token from data dictionary"""
    return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_access_token(token: str) -> dict:
    """Decode a JWT token and return the payload"""
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except Exception as e:
        logger.error(f"Failed to decode token: {e}")
        raise ValueError(f"Invalid token: {str(e)}")


async def authenticate_geotab_credentials(
    username: str, password: str, database_url: str
) -> dict:
    """Authenticate with Geotab using credentials and return JWT"""

    # Parse database URL: https://my.geotab.com/demo_geobase
    parts = database_url.strip().rsplit("/", 1)
    if len(parts) != 2:
        raise HTTPException(
            status_code=400,
            detail="Database URL must be: https://my.geotab.com/database_name",
        )

    server_url, database = parts[0], parts[1]
    # Extract server from URL (e.g., "my.geotab.com" from "https://my.geotab.com")
    server = server_url.replace("https://", "").replace("http://", "")

    try:
        # Use mygeotab SDK to authenticate
        api = mygeotab.API(
            username=username, password=password, database=database, server=server
        )

        # Authenticate
        api.authenticate()

        # Get user info using the authenticated session
        geotab_users = api.get("User", search={"name": username})

        if not geotab_users:
            raise HTTPException(status_code=401, detail="User not found")

        geotab_user = geotab_users[0]
        geotab_id = geotab_user.get("id")

        if not geotab_id:
            raise HTTPException(status_code=401, detail="No user id in response")

        # Return the authenticated API instance and user info
        return {"api": api, "user_id": geotab_id, "username": username}

    except mygeotab.exceptions.AuthenticationException as e:
        logger.error(f"Geotab authentication failed: {e}")
        raise HTTPException(status_code=401, detail=f"Authentication failed: {str(e)}")
    except mygeotab.exceptions.MyGeotabException as e:
        logger.error(f"Geotab API error: {e}")
        raise HTTPException(status_code=500, detail=f"Geotab API error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error during Geotab authentication: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
