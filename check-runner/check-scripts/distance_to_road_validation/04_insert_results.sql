-- Insert detailed results for each flagged location

INSERT INTO distance_to_road_results (distance, geotab_location_id, validation_id)
SELECT
    lwd.distance_meters,
    lwd.id,
    v.id
FROM locations_with_distance lwd
JOIN validation v ON v.geotab_database_id = lwd.geotab_database_id
WHERE v.validation_type = 'DISTANCE_TO_ROAD'
  AND v.finished_at > NOW() - INTERVAL '1 minute';
