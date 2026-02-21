import logging
from fastapi import HTTPException, status, Header
from dotenv import load_dotenv
import mygeotab
from typing import Optional

load_dotenv()

logger = logging.getLogger(__name__)


async def get_current_user(
    geotab_session_id: str = Header(..., description="Geotab session ID", alias="geotab-session-id"),
    geotab_database: str = Header(..., description="Geotab database name", alias="geotab-database"),
    geotab_username: str = Header(..., description="Geotab username", alias="geotab-username"),
    geotab_server: str = Header("my.geotab.com", description="Geotab server", alias="geotab-server"),
) -> dict:
    """Validate Geotab session_id and return user data from Geotab"""

    try:
        # Create API instance with session credentials
        api = mygeotab.API(
            username=geotab_username,
            session_id=geotab_session_id,
            database=geotab_database,
            server=geotab_server,
        )

        # Validate session by getting current user info
        user_results = api.get("User", search={"name": geotab_username})

        if not user_results:
            raise HTTPException(status_code=401, detail="User not found")

        user_data = user_results[0]

        logger.info(f"Session validated for user: {user_data.get('name')}")

        return {
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "email": user_data.get("name"),  # In Geotab, username is typically email
            "database": geotab_database,
            "server": geotab_server,
        }

    except mygeotab.exceptions.AuthenticationException as e:
        logger.error(f"Geotab session validation failed: {e}")
        raise HTTPException(status_code=401, detail=f"Invalid session: {str(e)}")
    except mygeotab.exceptions.MyGeotabException as e:
        logger.error(f"Geotab API error: {e}")
        raise HTTPException(status_code=500, detail=f"Geotab API error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error during session validation: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
