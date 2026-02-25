from sqlalchemy import Column, Float, ForeignKey, Integer

from database.database import Base


class TeleportationResult(Base):
    """Model for storing teleportation validation results."""

    __tablename__ = "teleportation_results"

    implied_speed_kmh = Column(Float, nullable=False)
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
