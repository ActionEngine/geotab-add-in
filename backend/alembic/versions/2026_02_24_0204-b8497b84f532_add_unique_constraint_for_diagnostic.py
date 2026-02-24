"""add unique constraint for diagnostic

Revision ID: b8497b84f532
Revises: 4f0118e0e771
Create Date: 2026-02-24 02:04:23.236562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'b8497b84f532'
down_revision: Union[str, Sequence[str], None] = '4f0118e0e771'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        'uq_externalid_geotabdbid', 'geotab_diagnostic',
        ['external_id', 'geotab_database_id']
    )


def downgrade() -> None:
    op.drop_constraint(
        'uq_externalid_geotabdbid', 'geotab_diagnostic', type_='unique'
    )
