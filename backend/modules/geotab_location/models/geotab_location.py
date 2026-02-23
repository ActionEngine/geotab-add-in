from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from geoalchemy2 import Geometry
from database.database import Base


class GeotabLocation(Base):
    __tablename__ = "geotab_location"
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime(timezone=True), nullable=False, index=True)
    device_id = Column(String, nullable=False, index=True)
    external_id = Column(String, nullable=False, index=True)
    geometry = Column(Geometry(geometry_type='POINT', srid=4326), nullable=True)
    speed = Column(Integer, nullable=False)
    geotab_database_id = Column(Integer, ForeignKey('geotab_database.id'), nullable=False, index=True)
