from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

from modules.database.database import Base

# Import your models here to ensure they are registered with Alembic
from modules.auth.models.user import User

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

DATABASE_URL = os.getenv("SYNC_DATABASE_URL")
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def include_object(object, name, type_, reflected, compare_to):
    """
    Exclude certain tables from migrations, such as PostGIS system tables.
    """

    # Exclude PostGIS system tables and Tiger Geocoder tables
    postgis_tables = {
        "spatial_ref_sys",
        "geography_columns",
        "geometry_columns",
        "raster_columns",
        "raster_overviews",
        "topology",
        "layer",
        # Tiger Geocoder tables
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
        "tract",
        "zcta5",
        "zip_lookup",
        "zip_lookup_all",
        "zip_lookup_base",
        "zip_state",
        "zip_state_loc",
    }

    if type_ == "table" and name in postgis_tables:
        return False
    return True


def run_migrations_offline():
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
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
