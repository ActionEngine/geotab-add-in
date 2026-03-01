# Check Runner Service

A Python service that runs SQL validation scripts against Geotab data in PostGIS.

## How It Works

1. **Configuration**: Checks defined in `CHECKS` dict in `check_runner.py`
2. **Scripts**: SQL files in `scripts/<folder>/` executed in filename order
3. **Execution**: Stages run sequentially in a transaction; different checks run concurrently
4. **Parameters**: SQL uses `%(param_name)s` placeholders, values from `CHECKS`

## Configuration Structure

```python
CHECKS = {
    "my-check-name": {           # Check identifier (for logging)
        "script_folder": "road-counter",  # Folder under scripts/ containing SQL
        "params": {              # Parameters passed to SQL
            "target_interval_end": "$NOW",  # Special marker → current time
            "target_interval_depth": timedelta(minutes=120),
            "validation_type": "MY_CHECK",
            "done": "DONE",
        },
    }
}
```

**Special parameter markers:**
- `"$NOW"` - Replaced with `datetime.now(tz=timezone.utc)` at runtime

**Interval pattern** (used for time-range queries):
- `*_interval_end` - The end timestamp of the interval
- `*_interval_depth` - Duration looking backward (timedelta)
- SQL calculates start as: `end - depth`

## Adding a New Check

### 1. Create SQL scripts in `scripts/<folder>/`

Files execute in filename-sorted order. Use temp tables to pass data between stages:

```sql
-- 01-cleanup.sql
DELETE FROM validation WHERE validation_type = %(validation_type)s;

-- 02-collect.sql
CREATE TEMP TABLE my_data AS
SELECT * FROM somewhere WHERE datetime >= %(target_interval_end)s - %(target_interval_depth)s;

-- 03-insert.sql
INSERT INTO validation (geotab_database_id, validation_type, status, total)
SELECT geotab_database_id, %(validation_type)s, %(done)s, COUNT(*)
FROM my_data
GROUP BY geotab_database_id;
```

### 2. Add entry to `CHECKS` in `check_runner.py`

```python
"my-new-check": {
    "script_folder": "my-folder",  # matches scripts/my-folder/
    "params": {
        "target_interval_end": "$NOW",
        "target_interval_depth": timedelta(minutes=60),
        "validation_type": "MY_NEW_CHECK",
        "done": "DONE",
    },
},
```

### 3. Reuse existing scripts with different parameters

Multiple checks can use the same `script_folder` with different params:

```python
"road-counter-2h": {
    "script_folder": "road-counter",
    "params": {"target_interval_depth": timedelta(minutes=120), ...}
},
"road-counter-realtime": {
    "script_folder": "road-counter", 
    "params": {"target_interval_depth": timedelta(minutes=15), ...}
},
```

## Running

```bash
# Once
cd check-runner && DATABASE_URL=... uv run -m check_runner

# As service (every 5 min via CHECK_INTERVAL_SECONDS)
cd backend && docker compose up -d check-runner
```
