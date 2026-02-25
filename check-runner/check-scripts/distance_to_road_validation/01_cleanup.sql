-- Delete existing validation results for databases that have recent location data
DELETE FROM validation
WHERE validation_type = 'DISTANCE_TO_ROAD'
  AND geotab_database_id IN (
      SELECT DISTINCT gl.geotab_database_id
      FROM geotab_location gl
      WHERE gl.datetime >= NOW() - %(interval)s
        AND gl.geometry IS NOT NULL
  );
