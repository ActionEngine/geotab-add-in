-- geotab_database_id, actionengine_segment_id, diagnostic_id, diagnostic_value_avg

CREATE TEMP TABLE historical_diagnostic_avg ON COMMIT DROP

-- ====================================================================
-- or persist table for debug purposes 
-- ====================================================================
-- DROP TABLE IF EXISTS historical_diagnostic_avg;
-- CREATE TABLE historical_diagnostic_avg
-- ====================================================================

AS

WITH segment_with_device AS (
  SELECT DISTINCT
      device_location.geotab_database_id,
      nearest_segment.actionengine_segment_id,
      device_location.device_id
  FROM geotab_location device_location
  CROSS JOIN LATERAL (
      SELECT os.id AS actionengine_segment_id
      FROM overture_segments os
      WHERE os.geotab_database_id = device_location.geotab_database_id
        AND os.geometry && ST_Expand(device_location.geometry, %(segment_proximity_filter)s)
      ORDER BY device_location.geometry <-> os.geometry
      LIMIT 1
  ) AS nearest_segment
  WHERE device_location.geometry IS NOT NULL
    AND device_location.datetime >= %(historical_interval_end)s - %(historical_interval_depth_minutes)s
    AND device_location.datetime < %(historical_interval_end)s
)
SELECT
    swd.geotab_database_id,
    swd.actionengine_segment_id,
    gsd.diagnostic_id,
    AVG(gsd.data) AS diagnostic_value_avg
FROM segment_with_device swd
JOIN geotab_status_data gsd
    ON swd.geotab_database_id = gsd.geotab_database_id
    AND swd.device_id = gsd.device_id
WHERE gsd.datetime >= %(historical_interval_end)s - %(historical_interval_depth_minutes)s
  AND gsd.datetime < %(historical_interval_end)s
  AND gsd.diagnostic_id = ANY(%(diagnostic_ids)s)
GROUP BY 1, 2, 3;
