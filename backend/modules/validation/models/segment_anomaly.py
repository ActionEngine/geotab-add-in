from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
)

from database.database import Base


class SegmentAnomaly(Base):
    """Road counter anomaly detection results per segment and diagnostic."""

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
    diagnostic_id = Column(String, nullable=False, index=True)
    target_avg = Column(Float, nullable=False)
    historical_avg = Column(Float, nullable=False)
    relative_deviation = Column(Float, nullable=False)
    is_warning = Column(Boolean, nullable=False, default=False)
    is_error = Column(Boolean, nullable=False, default=False)
