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

Use `%(param_name)s` syntax for named parameters. The runner substitutes values from a context dictionary.

**Important:** Parameter names must match exactly between the SQL and the context dict.

## Adding New Checks

1. Create a `.sql` file in `check-scripts/` directory
2. Use `%(param_name)s` for any parameters
3. Ensure scripts are read-only (SELECT only)
4. Update the `contexts` mapping in `check_runner.py` if the script requires parameters

## Running Locally

```bash
cd backend

# Set up environment (use same DB as backend but with postgresql:// driver)
export DATABASE_URL="postgresql://user:password@localhost:5432/geotab_db"

# Run directly
python check-runner/check_runner.py

# Run via Docker Compose
docker compose run --rm check-runner
```
