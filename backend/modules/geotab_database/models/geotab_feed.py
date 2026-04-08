from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database.database import Base


class GeotabFeed(Base):
    __tablename__ = "geotab_feed"
    id = Column(Integer, primary_key=True, index=True)
    geotab_database_id = Column(
        Integer, ForeignKey("geotab_database.id"), nullable=False, index=True
    )
    object_type = Column(String, nullable=False, index=True)
    feed_version = Column(String, nullable=True)
    last_sync = Column(DateTime(timezone=True), nullable=True)
