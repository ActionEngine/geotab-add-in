# Aspen Geotab Add-in Project

This is a monorepo containing multiple components for a Geotab add-in application that integrates with the Geotab fleet management platform. The project consists of a React-based frontend add-in, a FastAPI backend service, and a command-line data downloader tool.

## Project Structure

```
/home/robert/geotab-add-in/
├── add-in/              # React/TypeScript Geotab Add-in frontend
├── backend/             # FastAPI backend with PostgreSQL/PostGIS
├── geotab-downloader/   # Python CLI tool for downloading Geotab data
├── geotab-docs/         # Local copy of Geotab Developer documentation
└── .github/             # GitHub Actions workflows
```

## Subproject 1: Backend (FastAPI)

**Location:** `backend/`

A FastAPI-based backend service providing REST APIs for the Geotab add-in, with PostgreSQL/PostGIS database and a background feed polling service.

### Technology Stack
- **Python:** 3.13+
- **Web Framework:** FastAPI 0.129.0
- **Database:** PostgreSQL 16 with PostGIS extension
- **ORM:** SQLAlchemy 2.0.46 (async)
- **Migrations:** Alembic 1.18.4
- **Authentication:** JWT (python-jose)
- **Geotab Integration:** mygeotab 0.9.4
- **Additional Libraries:**
  - GeoAlchemy2, Shapely - Geospatial data
  - DuckDB - Analytics
  - asyncpg, psycopg2-binary - PostgreSQL drivers

### Build Commands
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run with Docker Compose (recommended for development)
docker compose up -d db           # Start database only
docker compose up -d              # Start all services
docker compose run --rm run-db-migrations  # Run migrations

# Run locally (requires database running)
uvicorn main:app --reload --host 0.0.0.0 --port 8004

# Alembic migrations
docker compose run --rm backend alembic upgrade head      # Upgrade
docker compose run --rm backend alembic downgrade -1      # Downgrade
docker compose run --rm backend alembic history           # View history
docker compose run -u $(id -u):$(id -g) --rm backend alembic revision --autogenerate -m "message"
```

### Code Organization
```
backend/
├── main.py                    # FastAPI application entry point
├── get_feeds.py              # Background feed polling service
├── docker-compose.yml        # Docker services configuration
├── Dockerfile                # Backend API container
├── Dockerfile.feeds          # Feed polling service container
├── requirements.txt          # Python dependencies
├── alembic.ini              # Alembic migration configuration
├── alembic/                 # Migration scripts
│   ├── env.py
│   └── versions/            # Migration files (timestamp-named)
├── database/
│   └── database.py          # SQLAlchemy engine, session, base
└── modules/                 # Feature modules
    ├── auth/                # Authentication module
    │   ├── services/auth.py
    │   └── dependencies/auth.py
    ├── geotab_database/     # Database management
    │   ├── models/
    │   ├── routers/
    │   ├── schemas/
    │   ├── services/
    │   └── dependencies/
    ├── geotab_location/     # Location/LogRecord data
    ├── geotab_status_data/  # Status data
    ├── geotab_diagnostic/   # Diagnostics
    └── overture_segments/   # Overture map segments
```

### Docker Services
- `db` - PostgreSQL 16 with PostGIS
- `backend` - FastAPI REST API (port 8004)
- `run-db-migrations` - One-shot migration runner
- `feeds` - Background feed polling service

### API Documentation
When running locally:
- Swagger UI: http://localhost:8004/docs
- ReDoc: http://localhost:8004/redoc

### Environment Variables
Copy `.env.example` to `.env` and configure:
- `DATABASE_URL` - PostgreSQL connection string
- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` - Database credentials
- `JWT_SECRET` - Secret key for JWT tokens
- `INGESTION_DAYS_LIMIT` - Data ingestion limit (default: 3 days)

---

## Subproject 2: Add-in (React Frontend)

**Location:** `add-in/app/`

A React-based Geotab add-in that provides a map visualization interface for Geotab vehicle data.

### Technology Stack
- **Runtime:** Node.js 24.11.1
- **Package Manager:** Yarn 4.12.0 (with Volta pinning)
- **Framework:** React 19.2.4, TypeScript 5.9.3
- **Build Tool:** Vite 7.3.1
- **UI Framework:** @geotab/zenith 3.5.0
- **Map:** MapLibre GL 5.18.0, react-map-gl 8.1.0
- **Data Fetching:** TanStack Query 5.90.21
- **Geotab API:** mg-api-js 3.0.0
- **Linting:** ESLint 10.0.0, Prettier 3.8.1

### Build Commands
```bash
cd add-in/app

# Install dependencies
yarn install

# Development server
yarn dev

# Production build
yarn build

# Preview production build
yarn preview

# Linting
yarn lint
```

### Code Organization
```
add-in/app/
├── index.html              # HTML entry point
├── vite.config.ts         # Vite configuration
├── tsconfig.json          # TypeScript configuration
├── package.json           # Dependencies and scripts
├── .yarnrc.yml            # Yarn configuration
├── src/
│   ├── main.tsx          # Application entry point
│   ├── app/
│   │   ├── App.tsx       # Main App component
│   │   └── style.css
│   ├── components/
│   │   ├── auth-dialog/  # Authentication dialog
│   │   ├── geotab-map/   # Map visualization
│   │   └── side-bar/     # Side panel
│   ├── api/
│   │   └── database.ts   # Database API calls
│   ├── hooks/
│   │   └── useFetch.ts   # Data fetching hooks
│   ├── provider/
│   │   └── query-provider.tsx  # React Query provider
│   ├── types/
│   │   ├── auth.ts       # TypeScript types
│   │   └── vehicle.ts
│   ├── utils/
│   │   └── geotabApi.ts  # Geotab API utilities
│   └── image/
│       └── vehicle-icon.tsx
└── aspen-addin.json      # Geotab add-in manifest
```

### Development Modes
The add-in supports two modes:
1. **Local Development** - Uses credentials from environment variables via `mg-api-js`
2. **Production** - Runs as a Geotab add-in with the global `geotab` object

### Environment Variables
Copy `.env-example` to `.env`:
- `VITE_BASE_URL` - Base URL for deployment
- `VITE_GEOTAB_EMAIL` - Geotab username for local dev
- `VITE_GEOTAB_PASSWORD` - Geotab password
- `VITE_GEOTAB_DATABASE` - Geotab database name
- `VITE_GEOTAB_SERVER` - Geotab server (default: my.geotab.com)

### Add-in Manifest
The `aspen-addin.json` file configures the add-in for Geotab MyGeotab:
- Name: "Aspen Add-In"
- Menu: "Aspen DQ"
- Production URL: AWS Amplify deployment

---

## Subproject 3: Geotab Downloader (CLI Tool)

**Location:** `geotab-downloader/`

A Python CLI tool that downloads Geotab entities and saves them locally as CSV files.

### Technology Stack
- **Python:** 3.13 (strictly required)
- **Package Manager:** uv (modern Python package manager)
- **Key Dependencies:**
  - `mygeotab==0.9.4` - Geotab API client
  - `pytest>=9.0.2` - Testing framework
  - `ruff>=0.15.2` - Linting and code formatting

### Build Commands
```bash
cd geotab-downloader

# Install dependencies
uv sync

# Run the CLI tool
uv run geotab-downloader -u <username> -p <password> -d <database>

# Run tests
uv run pytest

# Linting
uv run ruff check .
uv run ruff format .

# Check lockfile is up to date
uv lock --check
```

### Code Organization
```
geotab-downloader/
├── src/geotab_downloader/
│   ├── __init__.py      # Package init
│   ├── __main__.py      # CLI entry point
│   ├── client.py        # Geotab API client creation
│   └── download.py      # Entity download logic
├── tests/
│   ├── test_client.py   # Client tests
│   └── test_download.py # Download logic tests
├── pyproject.toml       # Project config, dependencies, pytest, ruff
└── uv.lock             # Locked dependency versions
```

### Supported Entities
The CLI downloads these Geotab entities to CSV:
- `Device` → `device.csv`
- `LogRecord` → `logrecord.csv`
- `StatusData` → `statusdata.csv`
- `Trip` → `trip.csv`
- `Diagnostic` → `diagnostic.csv`

### Configuration
- Configuration file: `pyproject.toml`
- Environment variables: `.env` file (see `.env.example`)
- Line length: 88 characters (ruff)
- Test discovery: `tests/` directory

---

## Development Conventions

### Code Style Guidelines

#### 1. Avoid Redundant Comments

Code should be self-explanatory.
Comments are good when they explain things that are not immediately obvious.
Otherwise, they are bad.
Because they create noise.

**Bad**

We already know that this is a context manager from `@contextmanager` decorator.
We don't need to duplicate this information in comments.
We also already now that this is connection pool, it is written in function name.
Also, more of a nitpick -- function name could be a little bit more self-explanatory
```
@contextmanager
def connection_pool(dsn: str, minconn: int = 1, maxconn: int = 20) -> Any:
    """Context manager for psycopg2 connection pool."""
    pool = psycopg2_pool.ThreadedConnectionPool(minconn=minconn, maxconn=maxconn, dsn=dsn)
    try:
        yield pool
    finally:
        pool.closeall()
```

**Better**

Function name is now self-explanatory enough. Doc string is not needed.
```
@contextmanager
def db_connection_pool(dsn: str, minconn: int = 1, maxconn: int = 20) -> Any:
    pool = psycopg2_pool.ThreadedConnectionPool(minconn=minconn, maxconn=maxconn, dsn=dsn)
    try:
        yield pool
    finally:
        pool.closeall()
```

**Bad**

It is clear enough from function name what function is doing.
```python
# Get device from geotab API
def get_device_from_geotab_api(api_client, device_id):
    api.client(...)
```

**Also bad:**

```python
def get_device_from_geotab_api(api_client, device_id):
    """Get device from geotab API.
    """
    api.client(...)
```

#### 2. Keep Try Blocks Minimal

Only include code that might raise exceptions in try blocks. This makes it easier to identify the source of errors and prevents catching exceptions from unrelated code.

**Bad:**
```python
try:
    this_may_raise_FooException()
    something_unrelated_to_the_exception()
except FooException:
    # handle the exception
```

**Better:**
```python
try:
    this_may_raise_FooException()
except FooException:
    # handle the exception
something_unrelated_to_the_exception()
```

**Also OK:**
```python
try:
    this_may_raise_FooException()
except FooException:
    # handle the exception
else:
    something_unrelated_to_the_exception()
```

#### 3. Follow PEP 8

All Python code must follow PEP 8 style guidelines.

#### 4. Tests Are Not a Package

**Never** add `__init__.py` to the `tests/` directory. Tests should remain a flat directory, not a Python package.

**Why:**
- Tests are not meant to be imported as a package
- pytest discovers tests by file pattern, not by package structure
- Keeping tests as a flat directory prevents accidental imports from test code
- Follows pytest best practices

**Bad:**
```
project/
├── src/
└── tests/
    ├── __init__.py          # WRONG - tests are not a package
    └── test_something.py
```

**Correct:**
```
project/
├── src/
└── tests/
    └── test_something.py    # No __init__.py needed
```

#### 5. Prefer Flat Functions Over Classes for Tests

Use plain functions for tests. Avoid wrapping tests in classes unless you specifically need:
- Inheritance for shared fixtures/setup
- Grouping related tests with shared state
- Mixins for test utilities

**Bad:**
```python
class TestGetDatabaseUrl:
    def test_valid_postgresql_url(self):
        ...
    
    def test_missing_database_url(self):
        ...
```

**Correct:**
```python
def test_get_database_url_valid():
    ...

def test_get_database_url_missing():
    ...
```

The flat approach is more readable and pytest-native.

#### 6. Split Tests Into Multiple Files

Prefer splitting tests into multiple files by function/component rather than grouping them in large classes within a single file.

**Why:**
- Easier to locate specific tests
- Smaller, focused files are more maintainable
- Better parallelization with pytest-xdist
- Clearer test organization

**Bad:**
```
tests/
└── test_everything.py          # 500+ lines, tests for everything
```

**Correct:**
```
tests/
├── test_database_url.py        # URL validation tests
├── test_connection_pool.py     # Connection pool tests
├── test_run_check.py           # Single script execution tests
├── test_run_all_checks.py      # Concurrent execution tests
└── test_main.py                # Integration tests
```

#### 7. Let It Crash (geotab-downloader and check-runner)

**Exceptions:** Don't write code to catch exceptions that you can't handle. If you don't know how to handle an exception, let it crash and let the developer fix the underlying issue rather than hiding it.

**Accessing dict fields:** If some field is expected to always be present, just access it directly instead of `dict.get()`. If the field is missing, it will raise a `KeyError`, which is good because it indicates a bug in the code that needs to be fixed, rather than silently returning None and potentially causing more subtle bugs down the line. If you are not sure if the field will always be present, then use `dict.get()`.

#### 8. Software Principles

- **YAGNI** (You Aren't Gonna Need It) - avoid over-engineering
- **KISS** (Keep It Simple, Stupid) - clarity over cleverness

#### 9. Fail Fast on Missing Environment Variables

- **Never** use `os.getenv()` with a default (e.g., `os.getenv("VAR", "default")`) for required configuration
- Use explicit validation with clear error messages to fail early during startup
- Prefer `os.environ["VAR"]` (raises `KeyError`) or explicit check:
  ```python
  # Good - explicit check with clear error message
  DATABASE_URL = os.environ.get("DATABASE_URL")
  if not DATABASE_URL:
      logger.error("DATABASE_URL environment variable is required")
      sys.exit(1)
  
  # Acceptable - KeyError is clear enough for simple cases
  DATABASE_URL = os.environ["DATABASE_URL"]
  
  # Bad - silent failure, cryptic error later
  DATABASE_URL = os.getenv("DATABASE_URL")  # Returns None if missing
  conn = psycopg2.connect(DATABASE_URL)     # Fails with confusing error
  ```
- Rationale: Missing env vars are deployment/config issues, not code bugs. Explicit failures produce cleaner logs (no stack traces) and flow through logging infrastructure properly.

### TypeScript Configuration
- Target: ES2020
- Strict mode enabled
- Path mapping: `@/*` → `./src/*`
- Module resolution: bundler

---

## Testing Strategy

### Geotab Downloader
- **Framework:** pytest
- **Test Location:** `geotab-downloader/tests/`
- **Configuration:** `pyproject.toml` under `[tool.pytest.ini_options]`
- **Run:** `uv run pytest`
- **Features:**
  - Verbose output
  - Strict markers
  - Short traceback format
  - Summary of all outcomes

### Backend
- Tests run via pytest in Docker container
- Integration with PostgreSQL for database tests

### Add-in
- ESLint for code quality
- TypeScript for compile-time type checking

---

## CI/CD (GitHub Actions)

### Workflows

1. **geotab-downloader-quality** (`.github/workflows/geotab-downloader.yml`)
   - Triggers on PRs modifying `geotab-downloader/**`
   - Runs on: ubuntu-slim
   - Steps:
     - Checkout code
     - Install uv
     - Check lockfile is up to date (`uv lock --check`)
     - Install dependencies (`uv sync`)
     - Run tests (`uv run pytest`)
     - Check CLI (`uv run geotab-downloader --help`)

2. **backend** (`.github/workflows/backend.yml`)
   - Triggers on PRs modifying `backend/**`
   - Runs on: ubuntu-latest
   - Steps:
     - Checkout code
     - Build backend Docker image
     - Build feed service Docker image

---

## VSCode Workspace Configuration

The project uses a multi-root workspace (`projects.code-workspace`):

```json
{
  "folders": [
    {"name": "--- REPO ROOT ---", "path": "."},
    {"name": "add-in", "path": "add-in"},
    {"name": "backend", "path": "backend"},
    {"name": "geotab-downloader", "path": "geotab-downloader"}
  ]
}
```

To configure Python interpreters for subprojects:
1. Open the workspace with `File → Open Workspace from File`
2. Each subproject has `.vscode/settings.json` with interpreter path:
   ```json
   {"python.defaultInterpreterPath": "./.venv/bin/python"}
   ```

---

## Security Considerations

1. **Environment Variables**:
   - All sensitive data in `.env` files (not committed)
   - `.env.example` files show required variables without values

2. **Authentication**:
   - Backend uses JWT tokens with `JWT_SECRET`
   - Geotab credentials are encoded and stored in database

3. **CORS**:
   - Backend allows all origins (`["*"]`) - configure for production

4. **Dependencies**:
   - Locked versions in `uv.lock` and `requirements.txt`
   - Regular security updates recommended

---

## Deployment

### Add-in
- Deployed to AWS Amplify
- URL: `https://main.d14o3o9kbo1n4h.amplifyapp.com`
- Configured in `aspen-addin.json`

### Backend
- Docker Compose for production deployment
- Services: PostgreSQL, FastAPI, Feed polling

### Geotab Downloader
- Command-line tool for local use
- Can be packaged as standalone executable

---

## Geotab Documentation

**Location:** `geotab-docs/developers.geotab.com/`

A local copy of the Geotab Developer documentation (https://developers.geotab.com/) for offline reference, stored in compressed Markdown format.

### Format
- **Compressed Markdown**: 503 `.md` files (~4.5MB, ~560KB zipped)
- Originally 506 HTML files (~35MB, ~9MB zipped)
- **Compression ratio**: 8x smaller uncompressed, 16x smaller compressed

### Contents
- **MyGeotab API**: 301 API objects, 27 API methods
- **MyAdmin API**: Admin API documentation
- **AddIns**: Add-in development guides
- **Zenith**: UI component library documentation
- **Drive**: Geotab Drive SDK

### Key Documentation Paths

```
geotab-docs/
├── developers.geotab.com/
│   ├── myGeotab/
│   │   ├── guides/concepts/           # MultiCall, core concepts
│   │   ├── addIns/developingAddIns/   # Add-in development guide
│   │   ├── apiReference/objects/      # Device, LogRecord, Trip, etc.
│   │   └── apiReference/methods/      # Get, Set, Add, Remove, etc.
│   ├── myAdmin/
│   ├── zenith/
│   └── INDEX.md                       # Quick reference index
└── sync-docs.py                       # Sync script for updates
```

### Usage
When analyzing Geotab-related code or implementing features, prefer reading from this local documentation over web fetching for faster access and no rate limits.

All internal links have been converted from `.html` to `.md` for seamless navigation.

### Updating Documentation

To update the documentation from new HTML sources:

```bash
# 1. Download new HTML docs from Geotab
python geotab-docs/download-docs.py --output geotab-docs-html

# 2. Convert to compressed Markdown
python geotab-docs/sync-docs.py --source geotab-docs-html/developers.geotab.com

# 3. (Optional) Remove HTML source
rm -rf geotab-docs-html
```

Or manually convert from existing HTML:

```bash
python geotab-docs/sync-docs.py --source /path/to/html/docs
```

The sync script (`sync-docs.py`) converts HTML to clean Markdown, preserving:
- Headers, lists, tables, and code blocks
- Internal links (converted `.html` → `.md`)
- Document structure and hierarchy
