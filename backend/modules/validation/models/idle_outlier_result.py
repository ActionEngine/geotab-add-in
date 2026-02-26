from sqlalchemy import Boolean, Column, ForeignKey, Integer

from database.database import Base


class IdleOutlierResult(Base):
    """Model for storing idle outlier validation results.

    A row here means the vehicle was stopped (speed ≤ threshold) at a location
    that falls outside all known idle clusters (traffic lights, junctions, etc.).
    """

    __tablename__ = "idle_outlier_results"

    geotab_location_id = Column(
        Integer,
        ForeignKey("geotab_location.id"),
        primary_key=True,
        index=True,
    )
    validation_id = Column(
        Integer,
        ForeignKey("validation.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    is_outlier = Column(Boolean, nullable=False, index=True)
