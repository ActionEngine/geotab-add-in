import asyncio

from modules.utils.utils import is_db_has_recent_data
from logging_config import configure_logger, configure_root_logging

from modules.validation.services.distance_validation import (
    run_single_distance_validation,
)

from modules.validation.services.teleportation_validation import (
    run_single_teleportation_validation,
)
from modules.validation.services.idle_outlier_validation import (
    run_single_idle_outlier_validation,
)

configure_root_logging()
logger = configure_logger(__name__)


# Run validation services
INTERVAL_SECONDS = 900  # 15 minutes

# List of validation functions
VALIDATION_TASKS = [
    run_single_distance_validation,
    run_single_teleportation_validation,
    run_single_idle_outlier_validation,
]


async def run_validation_cycle() -> None:
    """Validation cycle that runs all validation services in parallel every INTERVAL_SECONDS seconds"""

    while True:
        try:
            # 1. Check for data in the database (called once)
            if await is_db_has_recent_data():
                logger.info("Data found, starting validation batch...")

                # 2. Run all three functions in parallel
                await asyncio.gather(*(f() for f in VALIDATION_TASKS))

                logger.info("Validation batch completed.")

        except Exception as e:
            logger.exception(f"Error during validation cycle: {e}")

        # 3. Wait for the next cycle
        await asyncio.sleep(INTERVAL_SECONDS)


async def main() -> None:
    logger.info("Validation service starting...")

    await run_validation_cycle()


if __name__ == "__main__":
    asyncio.run(main())
