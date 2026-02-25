-- Find recent locations and compute distance to nearest road
-- Only keep locations where distance > warning_threshold

CREATE TEMP TABLE locations_with_distance AS
WITH recent AS (
    SELECT
        gl.id,
        gl.device_id,
        gl.geotab_database_id,
        gl.geometry AS geom
    FROM geotab_location gl
    WHERE gl.geometry IS NOT NULL
      AND gl.datetime >= NOW() - %(interval)s
)
SELECT
    rl.id,
    rl.device_id,
    rl.geotab_database_id,
    nearest.distance_meters
FROM recent rl
CROSS JOIN LATERAL (
    SELECT ST_Distance(rl.geom::geography, os.geometry::geography) AS distance_meters
    FROM overture_segments os
    WHERE os.geotab_database_id = rl.geotab_database_id
    ORDER BY rl.geom <-> os.geometry
    LIMIT 1
) AS nearest
WHERE nearest.distance_meters > %(warning_threshold)s;
