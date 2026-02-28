-- Compute segment-level anomalies with device list
-- Inserts into validation and road_counter_results tables

WITH comparison AS (
    -- Per-device, per-diagnostic comparison
    SELECT 
        COALESCE(h.geotab_database_id, t.geotab_database_id) AS geotab_database_id,
        COALESCE(h.actionengine_segment_id, t.actionengine_segment_id) AS actionengine_segment_id,
        t.device_id,  -- no device in historical interval
        COALESCE(h.diagnostic_id, t.diagnostic_id) AS diagnostic_id,
        t.diagnostic_value_avg AS current_value,
        h.diagnostic_value_avg AS reference_value,
        CASE 
            WHEN
                COALESCE(h.diagnostic_value_avg, 0) = 0
                AND COALESCE(t.diagnostic_value_avg, 0) = 0
                THEN 0
            WHEN COALESCE(h.diagnostic_value_avg, 0) = 0 THEN 1
            WHEN COALESCE(t.diagnostic_value_avg, 0) = 0 THEN 1
            ELSE
                ABS(t.diagnostic_value_avg - h.diagnostic_value_avg)
                /
                GREATEST(t.diagnostic_value_avg, h.diagnostic_value_avg)
        END
        AS value_deviation
    FROM historical_diagnostic_avg h
    FULL OUTER JOIN target_diagnostic_avg t
        USING (geotab_database_id, actionengine_segment_id, diagnostic_id)
),
-- Aggregate per segment: collect devices into array, diagnostics into vectors
segment_vectors AS (
    SELECT
        geotab_database_id,
        actionengine_segment_id,
        ARRAY[device_id] AS device_ids, -- this is a scalar value, but we keep it as a vector for historical compatibility
        ARRAY_AGG(diagnostic_id ORDER BY diagnostic_id) AS diagnostic_ids,
        ARRAY_AGG(current_value ORDER BY diagnostic_id) AS current_values,
        ARRAY_AGG(reference_value ORDER BY diagnostic_id) AS reference_values,
        ARRAY_AGG(value_deviation ORDER BY diagnostic_id) AS value_deviations,
        AVG(value_deviation) AS aggregate_deviation
    FROM comparison
    GROUP BY geotab_database_id, actionengine_segment_id, device_id
),
classification AS (
    SELECT 
        *,
        aggregate_deviation > %(warning_threshold)s 
            AND aggregate_deviation <= %(error_threshold)s AS is_warning,
        aggregate_deviation > %(error_threshold)s AS is_error
    FROM segment_vectors
),
validation_insert AS (
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
        geotab_database_id,
        NOW(),
        NOW(),
        %(validation_type)s,
        'DONE',
        COUNT(*) FILTER (WHERE is_warning),
        COUNT(*) FILTER (WHERE is_error),
        COUNT(*)
    FROM classification
    GROUP BY geotab_database_id
    RETURNING id, geotab_database_id
)
INSERT INTO road_counter_results (
    validation_id,
    geotab_database_id,
    segment_id,
    device_ids,
    diagnostic_ids,
    current_values,
    reference_values,
    value_deviations,
    aggregate_deviation,
    is_warning,
    is_error
)
SELECT 
    v.id,
    c.geotab_database_id,
    c.actionengine_segment_id AS segment_id,
    c.device_ids,
    c.diagnostic_ids,
    c.current_values,
    c.reference_values,
    c.value_deviations,
    c.aggregate_deviation,
    c.is_warning,
    c.is_error
FROM classification c
JOIN validation_insert v ON v.geotab_database_id = c.geotab_database_id;
