from sqlalchemy import Column, Integer, String, Enum, DateTime
from modules.geotab_database.enums import IngestionStatus
from database.database import Base


class GeotabDatabase(Base):
    __tablename__ = "geotab_database"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(collation="case_insensitive"), index=True, nullable=False)
    database_name = Column(String(collation="case_insensitive"), nullable=False)
    credentials = Column(String, nullable=False)
    ingestion_status = Column(
        Enum(IngestionStatus, native_enum=False),
        nullable=False,
        default=IngestionStatus.NONE,
    )
    last_sync = Column(DateTime, nullable=True)
