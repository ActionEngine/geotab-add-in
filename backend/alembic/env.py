from logging.config import fileConfig
import os
from dotenv import load_dotenv

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Load environment variables
load_dotenv()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Get DATABASE_URL from environment and convert async driver to sync
database_url = os.getenv(
    "DATABASE_URL", "postgresql://user:password@localhost:5432/geotab_db"
)
# Replace asyncpg with psycopg2 for Alembic (sync driver)
if "+asyncpg" in database_url:
    database_url = database_url.replace("+asyncpg", "")

# Override the sqlalchemy.url in alembic.ini with the environment variable
config.set_main_option("sqlalchemy.url", database_url)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from database.database import Base
from modules.geotab_database.models.geotab_database import GeotabDatabase  # noqa: F401
from modules.geotab_database.models.geotab_feed import GeotabFeed  # noqa: F401
from modules.geotab_location.models.geotab_location import GeotabLocation  # noqa: F401
from modules.geotab_status_data.models.geotab_status_data import (
    GeotabStatusData,
)  # noqa: F401
from modules.overture_segments.models.overture_segments import (
    OvertureSegments,
)  # noqa: F401

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# PostGIS and TIGER tables to ignore
POSTGIS_TABLES = {
    "spatial_ref_sys",
    "geometry_columns",
    "geography_columns",
    "raster_columns",
    "raster_overviews",
}

TIGER_TABLES = {
    "addr",
    "addrfeat",
    "bg",
    "county",
    "county_lookup",
    "countysub_lookup",
    "cousub",
    "direction_lookup",
    "edges",
    "faces",
    "featnames",
    "geocode_settings",
    "geocode_settings_default",
    "layer",
    "loader_lookuptables",
    "loader_platform",
    "loader_variables",
    "pagc_gaz",
    "pagc_lex",
    "pagc_rules",
    "place",
    "place_lookup",
    "secondary_unit_lookup",
    "state",
    "state_lookup",
    "street_type_lookup",
    "tabblock",
    "tabblock20",
    "topology",
    "tract",
    "zcta5",
    "zip_lookup",
    "zip_lookup_all",
    "zip_lookup_base",
    "zip_state",
    "zip_state_loc",
}

EXCLUDED_SCHEMAS = {"tiger", "tiger_data", "topology"}


def include_object(object, name, type_, reflected, compare_to):
    """
    Filter out PostGIS and TIGER schemas/tables from migrations.

    Returns False for objects that should be ignored by Alembic.
    """
    # Ignore objects from PostGIS-related schemas
    if hasattr(object, "schema") and object.schema in EXCLUDED_SCHEMAS:
        return False

    # Ignore PostGIS and TIGER tables in the public schema
    if type_ == "table" and name in (POSTGIS_TABLES | TIGER_TABLES):
        return False

    return True


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
