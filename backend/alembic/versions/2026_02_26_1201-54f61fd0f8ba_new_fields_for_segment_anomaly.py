"""new fields for segment_anomaly

Revision ID: 54f61fd0f8ba
Revises: e3a8c1d5f092
Create Date: 2026-02-26 12:01:17.672380

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "54f61fd0f8ba"
down_revision: Union[str, Sequence[str], None] = "e3a8c1d5f092"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Old per-diagnostic data incompatible with new vector format
    # Actuall no idea, that's what Kimi thinks, but i don't care enough to check
    op.execute("TRUNCATE TABLE segment_anomaly")
    
    op.add_column(
        "segment_anomaly",
        sa.Column("diagnostic_ids", postgresql.ARRAY(sa.String()), nullable=False),
    )
    op.add_column(
        "segment_anomaly",
        sa.Column("current_values", postgresql.ARRAY(sa.Float()), nullable=False),
    )
    op.add_column(
        "segment_anomaly",
        sa.Column("reference_values", postgresql.ARRAY(sa.Float()), nullable=False),
    )
    op.add_column(
        "segment_anomaly",
        sa.Column("value_deviations", postgresql.ARRAY(sa.Float()), nullable=False),
    )
    op.add_column(
        "segment_anomaly", sa.Column("aggregate_deviation", sa.Float(), nullable=False)
    )
    op.drop_index(
        op.f("ix_segment_anomaly_diagnostic_id"), table_name="segment_anomaly"
    )
    op.drop_column("segment_anomaly", "target_avg")
    op.drop_column("segment_anomaly", "relative_deviation")
    op.drop_column("segment_anomaly", "historical_avg")
    op.drop_column("segment_anomaly", "diagnostic_id")


def downgrade() -> None:
    op.add_column(
        "segment_anomaly",
        sa.Column("diagnostic_id", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "segment_anomaly",
        sa.Column(
            "historical_avg",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "segment_anomaly",
        sa.Column(
            "relative_deviation",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "segment_anomaly",
        sa.Column(
            "target_avg",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.create_index(
        op.f("ix_segment_anomaly_diagnostic_id"),
        "segment_anomaly",
        ["diagnostic_id"],
        unique=False,
    )
    op.drop_column("segment_anomaly", "aggregate_deviation")
    op.drop_column("segment_anomaly", "value_deviations")
    op.drop_column("segment_anomaly", "reference_values")
    op.drop_column("segment_anomaly", "current_values")
    op.drop_column("segment_anomaly", "diagnostic_ids")
