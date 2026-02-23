from sqlalchemy import ARRAY, Column, Float, Integer, String, ForeignKey, JSON
from geoalchemy2 import Geometry
from database.database import Base


class OvertureSegments(Base):
    __tablename__ = "overture_segments"
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, nullable=False, index=True, unique=True)
    geometry = Column(Geometry(geometry_type="LINESTRING", srid=4326), nullable=False)
    bbox = Column(JSON, nullable=False)
    geotab_database_id = Column(
        Integer, ForeignKey("geotab_database.id"), nullable=False, index=True
    )
    names = Column(JSON, nullable=True)
    class_code = Column(String, nullable=True)
    subtype = Column(String, nullable=True)
    road_surface = Column(JSON, nullable=True)
    speed_limits = Column(JSON, nullable=True)
