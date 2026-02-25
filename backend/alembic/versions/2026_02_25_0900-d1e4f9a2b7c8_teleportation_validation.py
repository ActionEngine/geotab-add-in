"""Teleportation validation

Revision ID: d1e4f9a2b7c8
Revises: d3f4a1b2c6e7
Create Date: 2026-02-25 09:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d1e4f9a2b7c8"
down_revision: Union[str, Sequence[str], None] = "d3f4a1b2c6e7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "teleportation_results",
        sa.Column("implied_speed_kmh", sa.Float(), nullable=False),
        sa.Column("geotab_location_id", sa.Integer(), nullable=False),
        sa.Column("validation_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["geotab_location_id"], ["geotab_location.id"]),
        sa.ForeignKeyConstraint(
            ["validation_id"], ["validation.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("geotab_location_id", "validation_id"),
    )
    op.create_index(
        op.f("ix_teleportation_results_geotab_location_id"),
        "teleportation_results",
        ["geotab_location_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_teleportation_results_validation_id"),
        "teleportation_results",
        ["validation_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        op.f("ix_teleportation_results_validation_id"),
        table_name="teleportation_results",
    )
    op.drop_index(
        op.f("ix_teleportation_results_geotab_location_id"),
        table_name="teleportation_results",
    )
    op.drop_table("teleportation_results")
