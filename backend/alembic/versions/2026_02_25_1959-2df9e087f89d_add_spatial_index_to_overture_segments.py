"""add spatial index to overture segments

Revision ID: 2df9e087f89d
Revises: d1e4f9a2b7c8
Create Date: 2026-02-25 19:59:20.941990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision: str = '2df9e087f89d'
down_revision: Union[str, Sequence[str], None] = 'd1e4f9a2b7c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_overture_segments_geometry "
        "ON overture_segments USING gist (geometry)"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        "DROP INDEX IF EXISTS idx_overture_segments_geometry"
    )
