import logging
import asyncio
import os
from datetime import datetime, timedelta
from sqlalchemy import select
import mygeotab
from modules.geotab_database.enums import IngestionStatus
from modules.geotab_database.models.geotab_database import GeotabDatabase
from modules.geotab_database.models.geotab_feed import GeotabFeed
from modules.auth.services.auth import create_access_token
from modules.geotab_location.services.geotab_location import (
    get_feed_log_records,
    log_record_to_geotab_location,
)
from modules.geotab_status_data.services.geotab_status_data import (
    get_feed_status_data,
    status_data_to_geotab_status_data,
)
from database.database import SessionLocal

logger = logging.getLogger(__name__)


async def get_database_by_email_and_name(
    email: str, database_name: str
) -> GeotabDatabase | None:
    """
    Get Geotab database entry by user email and database name.
    """

    async with SessionLocal() as session:
        result = await session.execute(
            select(GeotabDatabase).where(
                GeotabDatabase.email == email,
                GeotabDatabase.database_name == database_name,
            )
        )

        return result.scalars().first()


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

        is_new_entry = db_entry is None

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

    # Trigger log record ingestion in the background only for new entries
    if is_new_entry:
        asyncio.create_task(ingest_log_records(db_entry.id, email, password, database))
        asyncio.create_task(ingest_status_data(db_entry.id, email, password, database))
        logger.info(f"Background ingestion tasks started for database_id={db_entry.id}")

    return db_entry


async def ingest_log_records(
    geotab_database_id: int,
    email: str,
    password: str,
    database: str,
    server: str = "my.geotab.com",
) -> None:
    """
    Ingest all LogRecords from Geotab and save to geotab_location table.

    Args:
        geotab_database_id: ID of the geotab_database entry
        email: Geotab username/email
        password: Geotab password
        database: Geotab database name
        server: Geotab server (default: my.geotab.com)
    """
    logger.info(f"Starting log record ingestion for database_id={geotab_database_id}")

    # Update status to IN_PROGRESS
    async with SessionLocal() as session:
        result = await session.execute(
            select(GeotabDatabase).where(GeotabDatabase.id == geotab_database_id)
        )
        db_entry = result.scalars().first()

        if not db_entry:
            logger.error(f"GeotabDatabase {geotab_database_id} not found")
            return

        db_entry.ingestion_status = IngestionStatus.IN_PROGRESS
        await session.commit()

    try:
        # Get days limit from environment variable
        days_limit = int(os.getenv("INGESTION_DAYS_LIMIT", "30"))
        from_date = datetime.utcnow() - timedelta(days=days_limit)

        logger.info(
            f"Ingesting data from the past {days_limit} days (from {from_date.isoformat()})"
        )

        # Create Geotab API instance
        api = mygeotab.API(
            username=email,
            password=password,
            database=database,
            server=server,
        )

        # Authenticate
        api.authenticate()

        # Fetch and save records in batches to avoid memory issues
        batch_size = 50000
        total_ingested = 0
        last_id = None

        logger.info(f"Starting batch ingestion with batch_size={batch_size}")

        while True:
            # Fetch batch of LogRecords using offset pagination
            logger.info(f"Fetching batch at lastId={last_id}...")
            batch = api.get(
                "LogRecord",
                search={"fromDate": from_date.isoformat()},
                resultsLimit=batch_size,
                sort={
                    "sortBy": "id",
                    "sortDirection": "asc",
                    "offset": last_id,
                },
            )

            if not batch:
                logger.info(f"No more records at lastId {last_id}")
                break

            logger.info(f"Fetched {len(batch)} records, saving to database...")

            # Save batch to database immediately
            async with SessionLocal() as session:
                for log_record in batch:
                    try:
                        log_record_to_geotab_location(
                            session=session,
                            log_record=log_record,
                            geotab_database_id=geotab_database_id,
                        )
                    except Exception as e:
                        logger.warning(
                            f"Failed to process log record {log_record.get('id')}: {e}"
                        )
                        continue

                await session.commit()

            total_ingested += len(batch)
            logger.info(f"Saved batch successfully. Total ingested: {total_ingested}")

            # If we got fewer results than the limit, we've reached the end
            if len(batch) < batch_size:
                logger.info(
                    f"Last batch returned {len(batch)} records, ingestion complete"
                )
                break

            # Update lastId from the last record in the batch for next iteration
            last_record = batch[-1]
            last_id = last_record.get("id")

        logger.info(f"Fetched and saved {total_ingested} log records from Geotab")

        # Initialize GetFeed for future polling
        logger.info("Initializing GetFeed for polling...")
        _, feed_version = await get_feed_log_records(
            username=email,
            password=password,
            database=database,
            server=server,
            feed_version=None,
        )

        # Create feed entry with the baseline version for polling
        async with SessionLocal() as session:
            result = await session.execute(
                select(GeotabFeed).where(
                    GeotabFeed.geotab_database_id == geotab_database_id,
                    GeotabFeed.object_type == "LogRecord",
                )
            )
            feed_entry = result.scalars().first()

            if not feed_entry:
                feed_entry = GeotabFeed(
                    geotab_database_id=geotab_database_id,
                    object_type="LogRecord",
                    feed_version=feed_version,
                    last_sync=datetime.utcnow(),
                )
                session.add(feed_entry)
            else:
                feed_entry.feed_version = feed_version
                feed_entry.last_sync = datetime.utcnow()

            await session.commit()

        # Update status to DONE and set last_sync
        async with SessionLocal() as session:
            result = await session.execute(
                select(GeotabDatabase).where(GeotabDatabase.id == geotab_database_id)
            )
            db_entry = result.scalars().first()

            if db_entry:
                db_entry.ingestion_status = IngestionStatus.DONE
                db_entry.last_sync = datetime.utcnow()
                await session.commit()

        logger.info(
            f"Successfully ingested {total_ingested} log records "
            f"for database_id={geotab_database_id}"
        )

    except Exception as e:
        logger.error(f"Error during log record ingestion: {e}")

        # Update status back to NONE on failure
        async with SessionLocal() as session:
            result = await session.execute(
                select(GeotabDatabase).where(GeotabDatabase.id == geotab_database_id)
            )
            db_entry = result.scalars().first()

            if db_entry:
                db_entry.ingestion_status = IngestionStatus.NONE
                await session.commit()

        raise


async def ingest_status_data(
    geotab_database_id: int,
    email: str,
    password: str,
    database: str,
    server: str = "my.geotab.com",
) -> None:
    """
    Ingest all StatusData from Geotab and save to geotab_status_data table.

    Args:
        geotab_database_id: ID of the geotab_database entry
        email: Geotab username/email
        password: Geotab password
        database: Geotab database name
        server: Geotab server (default: my.geotab.com)
    """
    logger.info(f"Starting status data ingestion for database_id={geotab_database_id}")

    try:
        # Get days limit from environment variable
        days_limit = int(os.getenv("INGESTION_DAYS_LIMIT", "30"))
        from_date = datetime.utcnow() - timedelta(days=days_limit)

        logger.info(
            f"Ingesting status data from the past {days_limit} days (from {from_date.isoformat()})"
        )

        # Create Geotab API instance
        api = mygeotab.API(
            username=email,
            password=password,
            database=database,
            server=server,
        )

        # Authenticate
        api.authenticate()

        # Fetch and save records in batches to avoid memory issues
        batch_size = 500000
        total_ingested = 0
        last_date = None
        last_id = None

        logger.info(
            f"Starting status data batch ingestion with batch_size={batch_size}"
        )

        while True:
            # Fetch batch of StatusData using offset pagination
            logger.info(
                f"Fetching status data batch at offset={last_date}, lastId={last_id}..."
            )

            sort_params = {
                "sortBy": "date",
                "sortDirection": "asc",
            }
            if last_date is not None:
                sort_params["offset"] = last_date
            if last_id is not None:
                sort_params["lastId"] = last_id

            batch = api.get(
                "StatusData",
                search={"fromDate": from_date.isoformat()},
                resultsLimit=batch_size,
                sort=sort_params,
            )

            if not batch:
                logger.info(f"No more status data records at lastId {last_id}")
                break

            logger.info(
                f"Fetched {len(batch)} status data records, saving to database..."
            )

            # Save batch to database immediately
            async with SessionLocal() as session:
                for status_data in batch:
                    try:
                        status_data_to_geotab_status_data(
                            session=session,
                            status_data=status_data,
                            geotab_database_id=geotab_database_id,
                        )
                    except Exception as e:
                        logger.warning(
                            f"Failed to process status data {status_data.get('id')}: {e}"
                        )
                        continue

                await session.commit()

            total_ingested += len(batch)
            logger.info(
                f"Saved status data batch successfully. Total ingested: {total_ingested}"
            )

            # If we got fewer results than the limit, we've reached the end
            if len(batch) < batch_size:
                logger.info(
                    f"Last status data batch returned {len(batch)} records, ingestion complete"
                )
                break

            # Update offset and lastId from the last record in the batch for next iteration
            last_record = batch[-1]
            last_date = last_record.get("dateTime")
            last_id = last_record.get("id")

        logger.info(
            f"Fetched and saved {total_ingested} status data records from Geotab"
        )

        # Initialize GetFeed for future polling
        logger.info("Initializing GetFeed for status data polling...")
        _, feed_version = await get_feed_status_data(
            username=email,
            password=password,
            database=database,
            server=server,
            feed_version=None,
        )

        # Create feed entry with the baseline version for polling
        async with SessionLocal() as session:
            result = await session.execute(
                select(GeotabFeed).where(
                    GeotabFeed.geotab_database_id == geotab_database_id,
                    GeotabFeed.object_type == "StatusData",
                )
            )
            feed_entry = result.scalars().first()

            if not feed_entry:
                feed_entry = GeotabFeed(
                    geotab_database_id=geotab_database_id,
                    object_type="StatusData",
                    feed_version=feed_version,
                    last_sync=datetime.utcnow(),
                )
                session.add(feed_entry)
            else:
                feed_entry.feed_version = feed_version
                feed_entry.last_sync = datetime.utcnow()

            await session.commit()

        logger.info(
            f"Successfully ingested {total_ingested} status data records "
            f"for database_id={geotab_database_id}"
        )

    except Exception as e:
        logger.error(f"Error during status data ingestion: {e}")
        raise
