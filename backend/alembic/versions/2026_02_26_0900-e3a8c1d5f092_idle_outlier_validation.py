"""Idle outlier validation

Revision ID: e3a8c1d5f092
Revises: 69959752224f
Create Date: 2026-02-25 12:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import geoalchemy2

# revision identifiers, used by Alembic.
revision: str = "e3a8c1d5f092"
down_revision: Union[str, Sequence[str], None] = "69959752224f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade by creating tables for idle outlier validation results and precomputed idle clusters."""

    # Create tables for idle outlier validation results and precomputed idle clusters.
    op.create_table(
        "idle_outlier_results",
        sa.Column("geotab_location_id", sa.Integer(), nullable=False),
        sa.Column("validation_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["geotab_location_id"], ["geotab_location.id"]),
        sa.ForeignKeyConstraint(
            ["validation_id"], ["validation.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("geotab_location_id", "validation_id"),
    )
    op.create_index(
        op.f("ix_idle_outlier_results_geotab_location_id"),
        "idle_outlier_results",
        ["geotab_location_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_idle_outlier_results_validation_id"),
        "idle_outlier_results",
        ["validation_id"],
        unique=False,
    )
    # Create indexes on geotab_location for faster joins in validation queries
    op.create_table(
        "idle_clusters",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("geotab_database_id", sa.Integer(), nullable=False),
        sa.Column("cluster_id", sa.Integer(), nullable=False),
        sa.Column(
            "geometry",
            geoalchemy2.types.Geometry(geometry_type="GEOMETRY", srid=4326),
            nullable=False,
        ),
        sa.Column("point_count", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["geotab_database_id"], ["geotab_database.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_idle_clusters_id"), "idle_clusters", ["id"], unique=False)
    op.create_index(
        op.f("ix_idle_clusters_geotab_database_id"),
        "idle_clusters",
        ["geotab_database_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade by dropping the new tables and indexes."""

    op.drop_index(
        op.f("ix_idle_clusters_geotab_database_id"), table_name="idle_clusters"
    )
    op.drop_index(op.f("ix_idle_clusters_id"), table_name="idle_clusters")
    op.drop_table("idle_clusters")

    op.drop_index(
        op.f("ix_idle_outlier_results_validation_id"), table_name="idle_outlier_results"
    )
    op.drop_index(
        op.f("ix_idle_outlier_results_geotab_location_id"),
        table_name="idle_outlier_results",
    )
    op.drop_table("idle_outlier_results")
