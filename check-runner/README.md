# Check Runner Service

A Python service that runs SQL scripts against the GeoTab data in PostGIS.

## How It Works

1. Loads all checks from `check-scripts/` directory (each check is a subdirectory)
2. Each check can have multiple stages (SQL files within the subdirectory)
3. Stages within a check execute sequentially in a single transaction
4. Different checks run concurrently using a thread pool
5. Supports named parameters `%(param_name)s` in SQL
6. Reports results (row counts or errors)
7. Exits with code 1 if any check fails

## Check Structure

Checks are organized as directories under `check-scripts/`:

```
check-scripts/
├── distance_to_road_validation/     # Multi-stage check
│   ├── 01_cleanup.sql
│   ├── 02_compute_distances.sql
│   ├── 03_insert_validation.sql
│   ├── 04_insert_results.sql
│   └── 05_insert_by_device.sql
└── select_device_statuses/          # Single-stage check
    └── 01_select.sql
```

- **Check name**: Directory name
- **Stages**: SQL files within the directory, executed in filename-sorted order
- **State passing**: Use `CREATE TEMP TABLE` to share data between stages

## Multi-Stage Checks

For complex validations, split the logic into multiple stages:

```sql
-- 01_cleanup.sql
DELETE FROM validation WHERE validation_type = 'MY_CHECK';

-- 02_prepare.sql
CREATE TEMP TABLE flagged_records AS
SELECT * FROM some_table WHERE condition = true;

-- 03_insert.sql
INSERT INTO validation (geotab_database_id, validation_type, status, ...)
SELECT geotab_database_id, 'MY_CHECK', 'DONE', COUNT(*)
FROM flagged_records
GROUP BY geotab_database_id;
```

Benefits:
- Each stage is focused and readable (20-30 lines vs 100+ lines)
- Easy to debug by inspecting temp tables between stages
- Clear execution order via filename prefixes (01_, 02_, etc.)

## Parameters

Use `%(param_name)s` syntax for named parameters. Parameters are defined in `check_runner.py`:

```python
contexts = {
    "distance_to_road_validation": {
        "interval": timedelta(minutes=60),
        "warning_threshold": 5,
        "error_threshold": 10,
    },
}
```

## Adding New Checks

1. Create a new directory under `check-scripts/`
2. Add SQL files with numeric prefixes for ordering (e.g., `01_`, `02_`)
3. Use `CREATE TEMP TABLE` to pass data between stages
4. Update the `contexts` mapping in `check_runner.py` if parameters are needed

## Running Locally

```bash
cd backend

# Run directly
export DATABASE_URL="postgresql://user:password@localhost:5432/geotab_db"
cd check-runner && uv run -m check_runner

# Run via Docker Compose
cd backend && docker compose run --rm --build check-runner
```

## GeoTab API Reference

See `geotab-docs/developers.geotab.com/` for local GeoTab API documentation.
