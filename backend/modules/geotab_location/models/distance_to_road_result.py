from sqlalchemy import Column, Float, ForeignKey, Integer

from database.database import Base


class DistanceToRoadResult(Base):
    __tablename__ = "distance_to_road_results"

    distance = Column(Float, nullable=False)
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
