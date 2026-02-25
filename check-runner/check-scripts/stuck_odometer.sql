SELECT
    sd.device_id,
    MIN(sd.datetime) AS stuck_since,
    MAX(sd.datetime) AS last_seen,
    EXTRACT(EPOCH FROM (MAX(sd.datetime) - MIN(sd.datetime))) / 3600.0 AS hours_stuck,
    sd.data AS odometer_value
FROM geotab_status_data sd
JOIN geotab_diagnostic gd ON sd.diagnostic_id = gd.external_id
    AND sd.geotab_database_id = gd.geotab_database_id
WHERE gd.external_id = 'DiagnosticOdometerId'
    AND sd.geotab_database_id = 1
    AND sd.datetime >= NOW() - INTERVAL '24 hours'
GROUP BY sd.device_id, sd.data
HAVING MAX(sd.datetime) - MIN(sd.datetime) > INTERVAL '1 hour'
ORDER BY hours_stuck DESC;
