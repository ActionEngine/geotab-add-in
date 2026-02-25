-- Insert validation summary records

WITH stats AS (
    SELECT
        lwd.geotab_database_id,
        COUNT(*) AS flagged_count,
        COUNT(*) FILTER (WHERE lwd.distance_meters <= %(error_threshold)s) AS warning_count,
        COUNT(*) FILTER (WHERE lwd.distance_meters > %(error_threshold)s) AS error_count
    FROM locations_with_distance lwd
    GROUP BY lwd.geotab_database_id
),
total_counts AS (
    SELECT
        gl.geotab_database_id,
        COUNT(*) AS total_count
    FROM geotab_location gl
    WHERE gl.datetime >= NOW() - %(interval)s
      AND gl.geometry IS NOT NULL
    GROUP BY gl.geotab_database_id
)
INSERT INTO validation (
    geotab_database_id,
    started_at,
    finished_at,
    validation_type,
    status,
    warnings,
    errors,
    total
)
SELECT
    tc.geotab_database_id,
    NOW(),
    NOW(),
    'DISTANCE_TO_ROAD',
    'DONE',
    COALESCE(s.warning_count, 0),
    COALESCE(s.error_count, 0),
    tc.total_count
FROM total_counts tc
LEFT JOIN stats s ON s.geotab_database_id = tc.geotab_database_id
RETURNING id AS validation_id, geotab_database_id;
