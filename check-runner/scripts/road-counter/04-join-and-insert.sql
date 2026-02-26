-- Compute anomalies and insert into both validation and segment_anomaly tables

WITH target_segment_avg AS (
    SELECT
        geotab_database_id,
        actionengine_segment_id,
        diagnostic_id,
        AVG(diagnostic_value_avg) AS diagnostic_value_avg
    FROM target_diagnostic_avg
    GROUP BY 1, 2, 3
),
comparison AS (
    SELECT 
        t.geotab_database_id,
        t.actionengine_segment_id,
        t.diagnostic_id,
        t.diagnostic_value_avg AS target_avg,
        h.diagnostic_value_avg AS historical_avg,
        ABS(t.diagnostic_value_avg - h.diagnostic_value_avg) / 
            NULLIF(ABS(h.diagnostic_value_avg), 0) AS relative_deviation,
        ((%(diagnostics)s::jsonb)->t.diagnostic_id->>'warning_threshold')::numeric AS warning_threshold,
        ((%(diagnostics)s::jsonb)->t.diagnostic_id->>'error_threshold')::numeric AS error_threshold
    FROM target_segment_avg t
    JOIN historical_diagnostic_avg h 
        USING (geotab_database_id, actionengine_segment_id, diagnostic_id)
),
diagnostic_classification AS (
    SELECT
        geotab_database_id,
        actionengine_segment_id,
        diagnostic_id,
        target_avg,
        historical_avg,
        relative_deviation,
        relative_deviation > warning_threshold 
            AND relative_deviation <= error_threshold AS is_warning,
        relative_deviation > error_threshold AS is_error
    FROM comparison
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
        %(done)s,
        COUNT(*) FILTER (WHERE is_warning),
        COUNT(*) FILTER (WHERE is_error),
        COUNT(*)
    FROM diagnostic_classification
    GROUP BY geotab_database_id
    RETURNING id, geotab_database_id
)
INSERT INTO segment_anomaly (
    validation_id,
    geotab_database_id,
    segment_id,
    diagnostic_id,
    target_avg,
    historical_avg,
    relative_deviation,
    is_warning,
    is_error
)
SELECT 
    v.id,
    dc.geotab_database_id,
    dc.actionengine_segment_id AS segment_id,
    dc.diagnostic_id,
    dc.target_avg,
    dc.historical_avg,
    dc.relative_deviation,
    dc.is_warning,
    dc.is_error
FROM diagnostic_classification dc
JOIN validation_insert v ON v.geotab_database_id = dc.geotab_database_id;
