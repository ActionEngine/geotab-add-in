import asyncio
import logging

from modules.geotab_location.services.distance_validation import (
    run_distance_validation_service,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info("Distance validation service starting...")
    await run_distance_validation_service(interval_seconds=300)


if __name__ == "__main__":
    asyncio.run(main())
