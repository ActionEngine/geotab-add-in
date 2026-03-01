--output:
--     geotab_database_id
--     actionengine_segment_id
--     device_id
--     diagnostic_id
--     diagnostic_value_avg


CREATE TEMP TABLE target_diagnostic_avg ON COMMIT DROP

--====================================================================
--or persist table for debug purposes 
--====================================================================
-- --DROP TABLE IF EXISTS target_diagnostic_avg;
--CREATE TABLE target_diagnostic_avg
--====================================================================

AS

WITH location_filtered AS (
  SELECT
      geotab_database_id,
      device_id,
      geometry
  FROM geotab_location
  WHERE
    geometry IS NOT NULL
    AND datetime >= %(target_interval_end)s - %(target_interval_depth)s
    AND datetime < %(target_interval_end)s
),

segment_with_device AS (
  SELECT
      location_filtered.geotab_database_id,
      nearest_segment.actionengine_segment_id,
      location_filtered.device_id
  FROM location_filtered
  CROSS JOIN LATERAL (
      SELECT os.id AS actionengine_segment_id
      FROM overture_segments os
      WHERE os.geotab_database_id = location_filtered.geotab_database_id
        AND os.geometry && ST_Expand(location_filtered.geometry, %(segment_proximity_filter)s)
      ORDER BY location_filtered.geometry <-> os.geometry
      LIMIT 1
  ) AS nearest_segment
),

diagnostic_filtered AS (
    SELECT
        geotab_database_id,
        device_id,
        diagnostic_id,
        data AS diagnostic_value
    FROM geotab_status_data
    WHERE datetime >= %(target_interval_end)s - %(target_interval_depth)s
      AND datetime < %(target_interval_end)s
      AND diagnostic_id = ANY(%(diagnostic_ids)s)
)

SELECT
    seg2dev.geotab_database_id,
    seg2dev.actionengine_segment_id,
    seg2dev.device_id,
    diagnostic_id,
    AVG(diagnostic_value) AS diagnostic_value_avg
FROM segment_with_device seg2dev
JOIN diagnostic_filtered
    ON seg2dev.geotab_database_id = diagnostic_filtered.geotab_database_id
    AND seg2dev.device_id = diagnostic_filtered.device_id
GROUP BY 1, 2, 3, 4;
