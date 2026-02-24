from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String

from database.database import Base
from modules.geotab_location.enums import ValidationStatus


class Validation(Base):
    __tablename__ = "validation"

    id = Column(Integer, primary_key=True, index=True)
    geotab_database_id = Column(
        Integer,
        ForeignKey("geotab_database.id"),
        nullable=True,
        index=True,
    )
    started_at = Column(DateTime(timezone=True), nullable=False, index=True)
    finished_at = Column(DateTime(timezone=True), nullable=True)
    validation_type = Column(String, nullable=False, default="DISTANCE_TO_ROAD")
    warnings = Column(Integer, nullable=False, default=0)
    errors = Column(Integer, nullable=False, default=0)
    total = Column(Integer, nullable=False, default=0)
    status = Column(
        Enum(ValidationStatus, native_enum=False),
        nullable=False,
        default=ValidationStatus.IN_PROGRESS,
        index=True,
    )
