-- Insert per-device statistics

WITH params AS (
    SELECT
        %(warning_threshold)s AS warning_threshold,
        %(error_threshold)s AS error_threshold
),
device_totals AS (
    SELECT
        v.id AS validation_id,
        lwd.device_id,
        COUNT(*) AS total_count
    FROM locations_with_distance lwd
    JOIN validation v ON v.geotab_database_id = lwd.geotab_database_id
    WHERE v.validation_type = 'DISTANCE_TO_ROAD'
      AND v.finished_at > NOW() - INTERVAL '1 minute'
    GROUP BY v.id, lwd.device_id
),
device_flagged AS (
    SELECT
        v.id AS validation_id,
        lwd.device_id,
        COUNT(*) FILTER (WHERE lwd.distance_meters > p.warning_threshold AND lwd.distance_meters <= p.error_threshold) AS warning_count,
        COUNT(*) FILTER (WHERE lwd.distance_meters > p.error_threshold) AS error_count
    FROM locations_with_distance lwd
    JOIN validation v ON v.geotab_database_id = lwd.geotab_database_id
    JOIN params p ON TRUE
    WHERE v.validation_type = 'DISTANCE_TO_ROAD'
      AND v.finished_at > NOW() - INTERVAL '1 minute'
    GROUP BY v.id, lwd.device_id
)
INSERT INTO validation_results_by_device (validation_id, device_id, total, warnings, errors)
SELECT
    dt.validation_id,
    dt.device_id,
    dt.total_count,
    COALESCE(df.warning_count, 0),
    COALESCE(df.error_count, 0)
FROM device_totals dt
LEFT JOIN device_flagged df ON df.validation_id = dt.validation_id AND df.device_id = dt.device_id;
