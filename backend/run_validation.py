import asyncio
import logging

from modules.validation.services.distance_validation import (
    run_distance_validation_service,
)

from modules.validation.services.teleportation_validation import (
    run_teleportation_validation_service,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# Run validation services
INTERVAL_SECONDS = 300


async def main() -> None:
    logger.info("Distance validation service starting...")

    await asyncio.gather(
        run_distance_validation_service(interval_seconds=INTERVAL_SECONDS),
        run_teleportation_validation_service(interval_seconds=INTERVAL_SECONDS),
    )


if __name__ == "__main__":
    asyncio.run(main())
