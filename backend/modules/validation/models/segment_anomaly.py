from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import ARRAY

from database.database import Base


class SegmentAnomaly(Base):
    """Road counter anomaly detection"""

    __tablename__ = "segment_anomaly"

    id = Column(Integer, primary_key=True, index=True)
    validation_id = Column(
        Integer,
        ForeignKey("validation.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    geotab_database_id = Column(
        Integer,
        ForeignKey("geotab_database.id"),
        nullable=False,
        index=True,
    )
    segment_id = Column(
        Integer,
        ForeignKey("overture_segments.id"),
        nullable=False,
        index=True,
    )
    diagnostic_ids = Column(ARRAY(String), nullable=False)
    current_values = Column(ARRAY(Float), nullable=False)
    reference_values = Column(ARRAY(Float), nullable=False)
    value_deviations = Column(ARRAY(Float), nullable=False)
    aggregate_deviation = Column(Float, nullable=False)
    is_warning = Column(Boolean, nullable=False, default=False)
    is_error = Column(Boolean, nullable=False, default=False)
