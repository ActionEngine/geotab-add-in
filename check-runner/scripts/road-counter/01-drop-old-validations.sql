-- Delete old validations with the same type for affected databases
-- This ensures new validation replaces old validation
-- Cascade delete handles road_counter_results records

DELETE FROM validation
WHERE validation_type = %(validation_type)s
  AND geotab_database_id IN (
      SELECT DISTINCT geotab_database_id
      FROM geotab_location
      WHERE datetime >= %(target_interval_end)s - %(target_interval_depth_minutes)s
        AND datetime < %(target_interval_end)s
  );
