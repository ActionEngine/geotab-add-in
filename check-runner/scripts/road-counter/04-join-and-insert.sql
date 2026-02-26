-- Compute anomalies and insert into both validation and segment_anomaly tables
-- Aggregates per-diagnostic results into vectors per segment

WITH comparison AS (
    -- Per-diagnostic relative deviation
    SELECT 
        t.geotab_database_id,
        t.actionengine_segment_id,
        t.diagnostic_id,
        t.diagnostic_value_avg AS current_value,
        h.diagnostic_value_avg AS reference_value,
        ABS(t.diagnostic_value_avg - h.diagnostic_value_avg) / 
            NULLIF(ABS(h.diagnostic_value_avg), 0) AS value_deviation
    FROM target_diagnostic_avg t
    JOIN historical_diagnostic_avg h 
        USING (geotab_database_id, actionengine_segment_id, diagnostic_id)
),
-- Aggregate into vectors per segment with aggregate deviation
segment_vectors AS (
    SELECT 
        geotab_database_id,
        actionengine_segment_id,
        ARRAY_AGG(diagnostic_id ORDER BY diagnostic_id) AS diagnostic_ids,
        ARRAY_AGG(current_value ORDER BY diagnostic_id) AS current_values,
        ARRAY_AGG(reference_value ORDER BY diagnostic_id) AS reference_values,
        ARRAY_AGG(value_deviation ORDER BY diagnostic_id) AS value_deviations,
        AVG(value_deviation) AS aggregate_deviation
    FROM comparison
    GROUP BY geotab_database_id, actionengine_segment_id
),
-- Classify based on aggregate deviation vs single thresholds
classification AS (
    SELECT 
        *,
        aggregate_deviation > %(warning_threshold)s 
            AND aggregate_deviation <= %(error_threshold)s AS is_warning,
        aggregate_deviation > %(error_threshold)s AS is_error
    FROM segment_vectors
),
-- Insert validation summary per database
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
        %(done)s,
        COUNT(*) FILTER (WHERE is_warning),
        COUNT(*) FILTER (WHERE is_error),
        COUNT(*)
    FROM classification
    GROUP BY geotab_database_id
    RETURNING id, geotab_database_id
)
-- Insert segment-level anomaly data with vectors
INSERT INTO segment_anomaly (
    validation_id,
    geotab_database_id,
    segment_id,
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
    c.diagnostic_ids,
    c.current_values,
    c.reference_values,
    c.value_deviations,
    c.aggregate_deviation,
    c.is_warning,
    c.is_error
FROM classification c
JOIN validation_insert v ON v.geotab_database_id = c.geotab_database_id;
