from datetime import datetime, timedelta
import os

from sqlalchemy import text

from database.database import SessionLocal
from logging_config import configure_logger

logger = configure_logger(__name__)


RECENT_WINDOW_MINUTES = int(os.getenv("RECENT_WINDOW_MINUTES", "15"))


async def is_db_has_recent_data() -> bool:
    """Check if there are recent geotab_location rows in the database."""

    from_datetime = datetime.utcnow() - timedelta(minutes=RECENT_WINDOW_MINUTES)
    async with SessionLocal() as session:
        result = await session.execute(
            text("SELECT 1 FROM geotab_location " "WHERE datetime >= :from_dt LIMIT 1"),
            {"from_dt": from_datetime},
        )
        if result.scalar() is None:
            logger.info(
                "Skipping validation: no geotab_location data in the last %d minutes",
                RECENT_WINDOW_MINUTES,
            )
            return False

        return True
