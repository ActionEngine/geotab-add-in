import logging
import os


def resolve_log_level() -> tuple[int, str | None]:
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, None)
    if isinstance(level, int):
        return level, None

    return logging.INFO, level_name


def configure_root_logging() -> None:
    level, invalid_level = resolve_log_level()
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    if invalid_level:
        logging.getLogger(__name__).warning(
            "Invalid LOG_LEVEL=%s, falling back to INFO", invalid_level
        )


def configure_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    level, _ = resolve_log_level()
    logger.setLevel(level)
    return logger
