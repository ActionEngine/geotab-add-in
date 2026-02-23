from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from database.database import Base


class GeotabStatusData(Base):
    __tablename__ = "geotab_status_data"
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime(timezone=True), nullable=False, index=True)
    device_id = Column(String, nullable=False, index=True)
    external_id = Column(String, nullable=False, index=True)
    data = Column(Float, nullable=True)
    diagnostic_id = Column(String, nullable=False, index=True)
    version = Column(String, nullable=True)
    geotab_database_id = Column(Integer, ForeignKey('geotab_database.id'), nullable=False, index=True)
