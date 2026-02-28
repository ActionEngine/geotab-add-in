from datetime import datetime, timedelta
from functools import wraps
import os
from typing import Any

from sqlalchemy import text

from database.database import SessionLocal
from logging_config import configure_logger

logger = configure_logger(__name__)


RECENT_WINDOW_MINUTES = int(os.getenv("RECENT_WINDOW_MINUTES", "15"))


def require_recent_data(func):
    """Skip the wrapped coroutine if there are no recent geotab_location rows."""

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        from_datetime = datetime.utcnow() - timedelta(minutes=RECENT_WINDOW_MINUTES)
        async with SessionLocal() as session:
            result = await session.execute(
                text(
                    "SELECT 1 FROM geotab_location "
                    "WHERE datetime >= :from_dt LIMIT 1"
                ),
                {"from_dt": from_datetime},
            )
            if result.scalar() is None:
                logger.info(
                    "Skipping %s: no geotab_location data in the last %d minutes",
                    func.__name__,
                    RECENT_WINDOW_MINUTES,
                )
                return None

        return await func(*args, **kwargs)

    return wrapper
