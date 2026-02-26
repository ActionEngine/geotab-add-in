"""add device_ids to road_counter output

Revision ID: 746b2b7764cd
Revises: 54f61fd0f8ba
Create Date: 2026-02-26 15:39:20.791555

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '746b2b7764cd'
down_revision: Union[str, Sequence[str], None] = '54f61fd0f8ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


OLD_NAME = 'segment_anomaly'
NEW_NAME = 'road_counter_results'

def upgrade() -> None:
    op.execute(f"TRUNCATE TABLE {OLD_NAME}")
    op.add_column(
        OLD_NAME,
        sa.Column('device_ids', postgresql.ARRAY(sa.String()), nullable=False)
    )
    op.rename_table(OLD_NAME, NEW_NAME)


def downgrade() -> None:
    op.rename_table(NEW_NAME, OLD_NAME)
    op.drop_column(OLD_NAME, 'device_ids')
