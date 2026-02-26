-- output: geotab_database_id, actionengine_segment_id, device_id, diagnostic_id, diagnostic_value_avg

CREATE TEMP TABLE target_diagnostic_avg ON COMMIT DROP

-- ====================================================================
-- or persist table for debug purposes 
-- ====================================================================
--DROP TABLE IF EXISTS target_diagnostic_avg;
-- CREATE TABLE target_diagnostic_avg
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
    AND device_location.datetime >= %(target_interval_end)s - %(target_interval_depth_minutes)s
    AND device_location.datetime < %(target_interval_end)s
),
diagnostic_avg AS (
    SELECT
        geotab_database_id,
        device_id,
        diagnostic_id,
        AVG(data) AS diagnostic_value_avg
    FROM geotab_status_data
    WHERE datetime >= %(target_interval_end)s - %(target_interval_depth_minutes)s
      AND datetime < %(target_interval_end)s
      AND diagnostic_id = ANY(%(diagnostic_ids)s)
    GROUP BY 1, 2, 3
)
SELECT
    swl.geotab_database_id,
    swl.actionengine_segment_id,
    swl.device_id,
    diagnostic_avg.diagnostic_id,
    diagnostic_avg.diagnostic_value_avg
FROM segment_with_device swl
JOIN diagnostic_avg
    ON swl.geotab_database_id = diagnostic_avg.geotab_database_id
    AND swl.device_id = diagnostic_avg.device_id;
