"""geotab_diagnostic table

Revision ID: 4f0118e0e771
Revises: 915d46c4b375
Create Date: 2026-02-23 20:58:29.962999

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4f0118e0e771"
down_revision: Union[str, Sequence[str], None] = "915d46c4b375"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Those were always null anyway
    op.drop_index(
        op.f("ix_geotab_status_data_diagnostic_name"), table_name="geotab_status_data"
    )
    op.drop_column("geotab_status_data", "diagnostic_name")
    op.drop_column("geotab_status_data", "diagnostic_unit_of_measure")


    op.create_table(
        "geotab_diagnostic",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("external_id", sa.String(), nullable=False),
        sa.Column("geotab_database_id", sa.Integer(), nullable=False),
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
    op.add_column(
        "geotab_status_data", sa.Column("diagnostic_id", sa.String(), nullable=False)
    )
    op.create_index(
        op.f("ix_geotab_status_data_diagnostic_id"),
        "geotab_status_data",
        ["diagnostic_id"],
        unique=False,
    )


def downgrade() -> None:
    op.add_column(
        "geotab_status_data",
        sa.Column(
            "diagnostic_unit_of_measure",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "geotab_status_data",
        sa.Column("diagnostic_name", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_index(
        op.f("ix_geotab_status_data_diagnostic_id"), table_name="geotab_status_data"
    )
    op.create_index(
        op.f("ix_geotab_status_data_diagnostic_name"),
        "geotab_status_data",
        ["diagnostic_name"],
        unique=False,
    )
    op.drop_column("geotab_status_data", "diagnostic_id")
    op.drop_index(op.f("ix_geotab_diagnostic_id"), table_name="geotab_diagnostic")
    op.drop_index(
        op.f("ix_geotab_diagnostic_geotab_database_id"), table_name="geotab_diagnostic"
    )
    op.drop_index(
        op.f("ix_geotab_diagnostic_external_id"), table_name="geotab_diagnostic"
    )
    op.drop_table("geotab_diagnostic")
