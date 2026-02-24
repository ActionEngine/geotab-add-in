"""Distance to road by device table

Revision ID: d3f4a1b2c6e7
Revises: c157ece2f357
Create Date: 2026-02-24 17:05:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d3f4a1b2c6e7"
down_revision: Union[str, Sequence[str], None] = "c157ece2f357"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "validation_results_by_device",
        sa.Column("validation_id", sa.Integer(), nullable=False),
        sa.Column("device_id", sa.String(), nullable=False),
        sa.Column("total", sa.Integer(), nullable=False),
        sa.Column("warnings", sa.Integer(), nullable=False),
        sa.Column("errors", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["validation_id"], ["validation.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("validation_id", "device_id"),
    )
    op.create_index(
        op.f("ix_validation_results_by_device_validation_id"),
        "validation_results_by_device",
        ["validation_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_validation_results_by_device_device_id"),
        "validation_results_by_device",
        ["device_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        op.f("ix_validation_results_by_device_device_id"),
        table_name="validation_results_by_device",
    )
    op.drop_index(
        op.f("ix_validation_results_by_device_validation_id"),
        table_name="validation_results_by_device",
    )
    op.drop_table("validation_results_by_device")
