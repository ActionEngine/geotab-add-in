from geoalchemy2 import Geometry
from sqlalchemy import Column, ForeignKey, Integer

from database.database import Base


class IdleCluster(Base):
    """Precomputed convex-hull polygons for DBSCAN idle clusters.

    Populated during each idle-outlier validation run so that MVT tile
    queries can read pre-built geometries instead of re-running DBSCAN
    on every tile request.
    """

    __tablename__ = "idle_clusters"

    id = Column(Integer, primary_key=True, index=True)
    geotab_database_id = Column(
        Integer,
        ForeignKey("geotab_database.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    # DBSCAN-assigned cluster id (>= 0); unique per database but not globally.
    cluster_id = Column(Integer, nullable=False)
    # Convex hull of all idle points in this cluster, WGS-84.
    geometry = Column(Geometry(geometry_type="GEOMETRY", srid=4326), nullable=False)
    # Number of idle points that formed this cluster.
    point_count = Column(Integer, nullable=False)
