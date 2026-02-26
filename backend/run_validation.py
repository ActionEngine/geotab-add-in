import asyncio

from logging_config import configure_logger, configure_root_logging

from modules.validation.services.distance_validation import (
    run_distance_validation_service,
)

from modules.validation.services.teleportation_validation import (
    run_teleportation_validation_service,
)
from modules.validation.services.idle_outlier_validation import (
    run_idle_outlier_validation_service,
)

configure_root_logging()
logger = configure_logger(__name__)


# Run validation services
INTERVAL_SECONDS = 300


async def main() -> None:
    logger.info("Distance validation service starting...")

    await asyncio.gather(
        run_distance_validation_service(interval_seconds=INTERVAL_SECONDS),
        run_teleportation_validation_service(interval_seconds=INTERVAL_SECONDS),
        run_idle_outlier_validation_service(interval_seconds=INTERVAL_SECONDS),
    )


if __name__ == "__main__":
    asyncio.run(main())
