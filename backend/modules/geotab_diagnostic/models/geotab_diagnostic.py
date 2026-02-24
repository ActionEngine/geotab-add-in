from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from database.database import Base


class GeotabDiagnostic(Base):
    __tablename__ = "geotab_diagnostic"
    __table_args__ = (
        UniqueConstraint(
            "external_id", "geotab_database_id", name="uq_externalid_geotabdbid"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, nullable=False, index=True)
    geotab_database_id = Column(
        Integer, ForeignKey("geotab_database.id"), nullable=False, index=True
    )

    name = Column(String, nullable=False)
    unit_of_measure = Column(String, nullable=True)
    diagnostic_type = Column(String, nullable=False)
    source = Column(String, nullable=False)
