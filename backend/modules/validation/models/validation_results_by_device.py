from sqlalchemy import Column, ForeignKey, Integer, String

from database.database import Base


class DistanceToRoadByDevice(Base):
    __tablename__ = "validation_results_by_device"

    validation_id = Column(
        Integer,
        ForeignKey("validation.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    device_id = Column(String, primary_key=True, index=True)
    total = Column(Integer, nullable=False, default=0)
    warnings = Column(Integer, nullable=False, default=0)
    errors = Column(Integer, nullable=False, default=0)
