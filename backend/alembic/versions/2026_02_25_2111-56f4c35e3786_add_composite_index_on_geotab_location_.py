"""add composite index on geotab_location for datetime queries

Revision ID: 56f4c35e3786
Revises: 2df9e087f89d
Create Date: 2026-02-25 21:11:33.648678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56f4c35e3786'
down_revision: Union[str, Sequence[str], None] = '2df9e087f89d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create composite index for geotab_location datetime range queries."""
    op.create_index(
        'ix_geotab_location_db_datetime',
        'geotab_location',
        ['geotab_database_id', 'datetime'],
        postgresql_include=['device_id', 'geometry', 'speed', 'id'],
    )


def downgrade() -> None:
    """Drop composite index."""
    op.drop_index(
        'ix_geotab_location_db_datetime',
        table_name='geotab_location',
    )
