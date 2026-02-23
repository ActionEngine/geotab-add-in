"""Device table

Revision ID: d9495ab35e46
Revises: 72604a5fb799
Create Date: 2026-02-23 14:42:33.913320

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d9495ab35e46"
down_revision: Union[str, Sequence[str], None] = "72604a5fb799"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "geotab_diagnostic",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("geotab_database_id", sa.Integer(), nullable=False),
        sa.Column("external_id", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("unit_of_measure", sa.String(), nullable=True),
        sa.Column("diagnostic_type", sa.String(), nullable=False),
        sa.Column("source", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["geotab_database_id"],
            ["geotab_database.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_geotab_diagnostic_external_id"),
        "geotab_diagnostic",
        ["external_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_geotab_diagnostic_geotab_database_id"),
        "geotab_diagnostic",
        ["geotab_database_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_geotab_diagnostic_id"), "geotab_diagnostic", ["id"], unique=False
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_geotab_diagnostic_id"), table_name="geotab_diagnostic")
    op.drop_index(
        op.f("ix_geotab_diagnostic_geotab_database_id"), table_name="geotab_diagnostic"
    )
    op.drop_index(
        op.f("ix_geotab_diagnostic_external_id"), table_name="geotab_diagnostic"
    )
    op.drop_table("geotab_diagnostic")
