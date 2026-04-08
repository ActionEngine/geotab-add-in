"""
Geotab Feed Polling Service

This service continuously polls GetFeed for all registered feeds in the database
and saves new records to the geotab_location table.
"""

import asyncio
import os
import sys
from datetime import datetime, timezone

import mygeotab
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from logging_config import configure_logger, configure_root_logging

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.database import SessionLocal
from modules.geotab_database.models.geotab_feed import GeotabFeed
from modules.geotab_database.models.geotab_database import GeotabDatabase
from modules.geotab_diagnostic.models.geotab_diagnostic import GeotabDiagnostic
from modules.geotab_location.services.geotab_location import (
    get_feed_log_records,
    log_record_to_geotab_location,
)
from modules.geotab_status_data.services.geotab_status_data import (
    get_feed_status_data,
    status_data_to_geotab_status_data,
)
from modules.auth.services.auth import decode_access_token

configure_root_logging()
logger = configure_logger(__name__)


async def poll_single_feed(feed_id: int, poll_interval: int = 30) -> None:
    """
    Poll a single feed for new data.
    
    Args:
        feed_id: ID of the GeotabFeed entry
        poll_interval: Seconds between polls (default: 30)
    """

    logger.info(f"Starting polling for feed_id={feed_id}")

    while True:
        try:
            # Get feed entry and associated database
            async with SessionLocal() as session:
                result = await session.execute(
                    select(GeotabFeed, GeotabDatabase)
                    .join(GeotabDatabase, GeotabFeed.geotab_database_id == GeotabDatabase.id)
                    .where(GeotabFeed.id == feed_id)
                )
                row = result.first()
                
            if not row:
                logger.error(f"Feed {feed_id} not found, stopping polling")
                return
                
            feed_entry, db_entry = row
            feed_version = feed_entry.feed_version
            object_type = feed_entry.object_type
            
            # Decode credentials to get username and password
            credentials = decode_access_token(db_entry.credentials)
            email = credentials.get("email")
            password = credentials.get("password")
            database = credentials.get("database")
            
            if not all([email, password, database]):
                logger.error(f"Invalid credentials for feed {feed_id}")
                await asyncio.sleep(poll_interval)
                continue

            api = mygeotab.API(
                username=email,
                password=password,
                database=database,
            )
            api.authenticate()
            # Set last_sync time
            current_time = datetime.now(timezone.utc)
            # Handle different object types
            if object_type == "LogRecord":
                # Fetch new log records using GetFeed
                log_records, new_version = await get_feed_log_records(
                    api,
                    feed_version=feed_version,
                )
                
                # Insert new log records into database
                if log_records:
                    logger.info(f"Feed {feed_id} found {len(log_records)} new records")
                    
                    async with SessionLocal() as session:
                        for log_record in log_records:
                            try:
                                log_record_to_geotab_location(
                                    session=session,
                                    log_record=log_record,
                                    geotab_database_id=feed_entry.geotab_database_id,
                                )
                            except Exception as e:
                                logger.warning(f"Failed to process record {log_record.get('id')}: {e}")
                                continue
                        
                        await session.commit()
                
                # Update feed version and last_sync
                async with SessionLocal() as session:
                    result = await session.execute(
                        select(GeotabFeed).where(GeotabFeed.id == feed_id)
                    )
                    feed_entry: GeotabFeed = result.scalars().first()
                    
                    if feed_entry:
                        feed_entry.feed_version = new_version
                        feed_entry.last_sync = current_time
                        await session.commit()

                # Update last_sync for the database entry
                async with SessionLocal() as session:
                    result = await session.execute(
                        select(GeotabDatabase).where(GeotabDatabase.id == feed_entry.geotab_database_id)
                    )
                    db_entry: GeotabDatabase = result.scalars().first()
                    
                    if db_entry:
                        db_entry.last_sync = current_time
                        await session.commit()
            
            elif object_type == "StatusData":
                # Fetch new status data using GetFeed
                status_data_list, new_version = await get_feed_status_data(
                    api,
                    feed_version=feed_version,
                )
                
                # Insert new status data into database
                if status_data_list:
                    logger.info(f"Feed {feed_id} found {len(status_data_list)} new status data records")
                    
                    async with SessionLocal() as session:
                        for status_data in status_data_list:
                            status_data_to_geotab_status_data(
                                session=session,
                                status_data=status_data,
                                geotab_database_id=feed_entry.geotab_database_id,
                            )
                        
                        await session.commit()

                # Update feed version and last_sync
                async with SessionLocal() as session:
                    result = await session.execute(
                        select(GeotabFeed).where(GeotabFeed.id == feed_id)
                    )
                    feed_entry: GeotabFeed = result.scalars().first()
                    
                    if feed_entry:
                        feed_entry.feed_version = new_version
                        feed_entry.last_sync = current_time
                        await session.commit()

                # Update last_sync for the database entry
                async with SessionLocal() as session:
                    result = await session.execute(
                        select(GeotabDatabase).where(GeotabDatabase.id == feed_entry.geotab_database_id)
                    )
                    db_entry: GeotabDatabase = result.scalars().first()
                    
                    if db_entry:
                        db_entry.last_sync = current_time
                        await session.commit()

                diagnostic_ids = set(sd["diagnostic"]["id"] for sd in status_data_list)
                diagnostic_objects: list[dict] = api.get("Diagnostic", ids=list(diagnostic_ids))
                to_insert = [
                    dict(
                        geotab_database_id=feed_entry.geotab_database_id,
                        external_id=obj["id"],
                        name=obj["name"],
                        unit_of_measure=obj.get("unitOfMeasure"),
                        diagnostic_type=obj["diagnosticType"],
                        source=obj["source"],
                    )
                    for obj in diagnostic_objects
                ]
                insert_stmt = insert(GeotabDiagnostic).values(to_insert)
                on_conflict_stmt = insert_stmt.on_conflict_do_update(
                    index_elements=[
                        GeotabDiagnostic.geotab_database_id,
                        GeotabDiagnostic.external_id,
                    ],
                    set_={
                        "name": insert_stmt.excluded.name,
                        "unit_of_measure": insert_stmt.excluded.unit_of_measure,
                        "diagnostic_type": insert_stmt.excluded.diagnostic_type,
                        "source": insert_stmt.excluded.source,
                    },
                )

                async with SessionLocal() as session:
                    await session.execute(on_conflict_stmt)
                    await session.commit()

            else:
                logger.warning(f"Unsupported object type: {object_type}")
            
            # Wait before next poll
            await asyncio.sleep(poll_interval)
        
        except Exception as e:
            logger.error(f"Error polling feed {feed_id}: {e}", exc_info=True)
            # Wait before retrying
            await asyncio.sleep(poll_interval)


async def discover_and_poll_feeds(poll_interval: int = 30) -> None:
    """
    Discover all feeds in the database and start polling them.
    
    Args:
        poll_interval: Seconds between polls for each feed (default: 30)
    """
    logger.info("Starting feed discovery service")
    
    active_tasks = {}

    while True:
        try:
            # Get all feeds from database
            async with SessionLocal() as session:
                result = await session.execute(select(GeotabFeed))
                feeds = result.scalars().all()

            current_feed_ids = {feed.id for feed in feeds}
            
            # Start tasks for new feeds
            for feed in feeds:
                if feed.id not in active_tasks:
                    logger.info(f"Starting polling task for new feed {feed.id} (type: {feed.object_type})")
                    task = asyncio.create_task(poll_single_feed(feed.id, poll_interval))
                    active_tasks[feed.id] = task
            
            # Cancel tasks for removed feeds
            for feed_id in list(active_tasks.keys()):
                if feed_id not in current_feed_ids:
                    logger.info(f"Cancelling polling task for removed feed {feed_id}")
                    active_tasks[feed_id].cancel()
                    del active_tasks[feed_id]
            
            # Check for completed/failed tasks
            for feed_id in list(active_tasks.keys()):
                task = active_tasks[feed_id]
                if task.done():
                    try:
                        await task
                    except asyncio.CancelledError:
                        logger.info(f"Task for feed {feed_id} was cancelled")
                    except Exception as e:
                        logger.error(f"Task for feed {feed_id} failed: {e}")
                    del active_tasks[feed_id]
            
            # Wait before checking for new feeds
            await asyncio.sleep(60)  # Check for new feeds every minute
        
        except Exception as e:
            logger.error(f"Error in feed discovery: {e}", exc_info=True)
            await asyncio.sleep(60)


async def main():
    """Main entry point for the feed polling service."""
    try:
        logger.info("Geotab Feed Polling Service starting...")
        await discover_and_poll_feeds()
    except KeyboardInterrupt:
        logger.info("Service stopped by user")


if __name__ == "__main__":
    asyncio.run(main())
