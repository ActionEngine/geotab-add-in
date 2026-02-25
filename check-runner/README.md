# Check Runner Service

A Python service that runs SQL scripts against the GeoTab data in PostGIS.

## How It Works

1. Loads all `.sql` files from `check-scripts/` directory
2. Executes them concurrently using a thread pool
3. Supports named parameters `%(param_name)s` in SQL
4. Reports results (row counts or errors)
5. Exits with code 1 if any check fails

## SQL Script Format

Scripts are plain SQL files with optional named parameters:

```sql
-- Simple script with no parameters
SELECT * FROM geotab_status_data WHERE status = 'critical';
```

```sql
-- Script with named parameters
SELECT * FROM device_statuses
WHERE device_id = %(device_id)s
  AND recorded_at > NOW() - INTERVAL '%(hours)s hours';
```

## Parameters

Use `%(param_name)s` syntax for named parameters.

## Adding New Checks

1. Create a `.sql` file in `check-scripts/` directory
2. Use `%(param_name)s` for any parameters
3. Update the `contexts` mapping in `check_runner.py` if the script requires parameters

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
