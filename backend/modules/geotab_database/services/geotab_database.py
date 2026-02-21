import logging
from sqlalchemy import select
from backend.modules.geotab_database.enums import IngestionStatus
from modules.geotab_database.models.geotab_database import GeotabDatabase
from modules.auth.services.auth import create_access_token
from database.database import SessionLocal

logger = logging.getLogger(__name__)


async def add_or_replace_database(
    email: str, password: str, database: str
) -> GeotabDatabase:
    """
    Add or replace a Geotab database entry for a given email.
    Creates a JWT token from the password and stores it in credentials.
    """
    logger.debug(f"add_or_replace_database: email={email}, database={database}")

    # Create JWT token from password
    credentials_token = create_access_token(
        {"email": email, "password": password, "database": database}
    )

    async with SessionLocal() as session:
        # Check if database entry exists for this email and database
        result = await session.execute(
            select(GeotabDatabase).where(
                GeotabDatabase.email == email, GeotabDatabase.database_name == database
            )
        )
        db_entry = result.scalars().first()

        if db_entry:
            # Update existing entry
            logger.info(f"Updating existing database entry for email={email}")
            db_entry.database_name = database
            db_entry.credentials = credentials_token
        else:
            # Create new entry
            logger.info(f"Creating new database entry for email={email}")
            db_entry = GeotabDatabase(
                email=email,
                database_name=database,
                credentials=credentials_token,
                ingestion_status=IngestionStatus.NONE,
            )
            session.add(db_entry)

        await session.commit()
        await session.refresh(db_entry)
        logger.info(f"Database entry saved: id={db_entry.id}, email={db_entry.email}")

        return db_entry
