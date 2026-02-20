import logging
import os
from fastapi import HTTPException, status, Request, Response
from jose import jwt, JWTError
from dotenv import load_dotenv
from sqlalchemy import select
import httpx

from modules.auth.models.user import User
from modules.database.database import SessionLocal

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "supersecret")
JWT_ALGORITHM = "HS256"

logger = logging.getLogger(__name__)


def create_access_token(data: dict) -> str:
    return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)


async def get_current_user(request: Request) -> User:
    """Extract JWT, validate, and return User from database"""

    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated"
        )

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        logger.debug(f"JWT decoded, user_id from token: {user_id}")
    except JWTError as e:
        logger.error(f"JWT decode error: {e}")
        raise HTTPException(status_code=401, detail="Invalid token")

    # check if user exists in database
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.geotab_id == user_id))
        user = result.scalars().first()
        logger.debug(f"User from DB: {user}")
        if not user:
            logger.warning(f"User not found in DB for geotab_id: {user_id}")
            raise HTTPException(status_code=401, detail="User not found")
        logger.info(
            f"User found: id={user.id}, geotab_id={user.geotab_id}, email={user.email}"
        )
        return user


async def get_or_create_user(geotab_id: str, email: str | None = None) -> User:
    """Get existing user or create new one"""

    logger.debug(f"get_or_create_user: geotab_id={geotab_id}, email={email}")
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.geotab_id == geotab_id))
        user = result.scalars().first()
        if not user:
            logger.info(f"Creating new user: geotab_id={geotab_id}, email={email}")
            user = User(geotab_id=geotab_id, email=email)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            logger.info(f"User created: id={user.id}, geotab_id={user.geotab_id}")
        else:
            logger.debug(f"User exists: id={user.id}, geotab_id={user.geotab_id}")

        return user


def create_token_response(user: User) -> dict:
    """Create standardized token response"""

    token = create_access_token({"user_id": user.geotab_id})
    logger.info(f"Token created for user_id={user.geotab_id}, email={user.email}")
    return {"access_token": token, "user_id": user.geotab_id, "email": user.email}


def set_auth_cookie(response: Response, token: str) -> None:
    """Set authentication token in httponly cookie"""
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        samesite="lax",
        max_age=86400 * 7,  # 7 days
    )


async def verify_geotab_token(geotab_token: str) -> dict:
    """Verify Geotab OAuth token and return JWT"""

    async with httpx.AsyncClient() as client:
        userinfo_resp = await client.get(
            "https://my.geotab.com/apiv1/userinfo",
            headers={"Authorization": f"Bearer {geotab_token}"},
        )
        if userinfo_resp.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid Geotab token")

        userinfo = userinfo_resp.json()
        geotab_id = userinfo.get("sub") or userinfo.get("id")
        email = userinfo.get("email")
        if not geotab_id:
            raise HTTPException(status_code=401, detail="No user id in Geotab userinfo")

    user = await get_or_create_user(geotab_id, email)

    return create_token_response(user)


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

    server, database = parts[0], parts[1]

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            # Authenticate
            auth_resp = await client.post(
                f"{server}/apiv1",
                json={
                    "method": "Authenticate",
                    "params": {
                        "userName": username,
                        "password": password,
                        "database": database,
                    },
                },
            )

            if auth_resp.status_code != 200:
                raise HTTPException(
                    status_code=401,
                    detail=f"Failed to authenticate (HTTP {auth_resp.status_code})",
                )

            auth_data = auth_resp.json()
            if "error" in auth_data:
                raise HTTPException(
                    status_code=401,
                    detail=f"Geotab: {auth_data['error'].get('message', 'Unknown error')}",
                )

            credentials = auth_data.get("result", {}).get("credentials")
            if not credentials:
                raise HTTPException(status_code=401, detail="No credentials returned")

            # Get user info
            user_resp = await client.post(
                f"{server}/apiv1",
                json={
                    "method": "Get",
                    "params": {
                        "typeName": "User",
                        "credentials": credentials,
                        "search": {"name": credentials.get("userName")},
                    },
                },
            )

            if user_resp.status_code != 200:
                raise HTTPException(status_code=401, detail="Failed to get user info")

            user_data = user_resp.json()
            if "error" in user_data:
                raise HTTPException(
                    status_code=401,
                    detail=f"Geotab: {user_data['error'].get('message', 'Unknown error')}",
                )

            geotab_users = user_data.get("result", [])
            if not geotab_users:
                raise HTTPException(status_code=401, detail="User not found")

            geotab_user = geotab_users[0]
            geotab_id = geotab_user.get("id")
            email = geotab_user.get("name")

            if not geotab_id:
                raise HTTPException(status_code=401, detail="No user id in response")

    except httpx.ConnectError:
        raise HTTPException(status_code=503, detail=f"Cannot connect to '{server}'")
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail=f"Timeout connecting to '{server}'")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    user = await get_or_create_user(geotab_id, email)

    return create_token_response(user)
