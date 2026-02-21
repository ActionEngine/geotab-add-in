# Geotab Add-in Backend

## Local Development Setup

### Prerequisites

- Python 3.13+
- Docker and Docker Compose
- pip

### 1. Create Virtual Environment

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment
python -m venv venv

# Or using conda
conda create -n geotab-add-in python=3.13
```

### 2. Activate Environment

```bash
# Using venv (Linux/Mac)
source venv/bin/activate

# Using venv (Windows)
venv\Scripts\activate

# Using conda
conda activate geotab-add-in
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file and update it with your settings:

```bash
cp .env.example .env
```

Edit the `.env` file to customize your database credentials and other settings if needed. The default values are suitable for local development.

### 5. Run Alembic Migrations

Run database migrations within container Docker:

```bash
# Apply all pending migrations
docker compose run --rm backend alembic upgrade head

# Rollback one migration
docker compose run --rm backend alembic downgrade -1

# Rollback all migrations
docker compose run --rm backend alembic downgrade base

# View migration history
docker compose run --rm backend alembic history
```

### 6. Run the Backend Server for debug (Optional)

### 6.1 Start database container

Start only the PostgreSQL database using Docker Compose:

```bash
docker compose run db
```

### 6.2 Run the application with unicorn or using VSCode debugger

**Note:** Ensure the database host in `.env` is set to `localhost` (not `db`) when running the backend server locally:

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/geotab_db
```

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8004
```

The API will be available at http://localhost:8004

API documentation will be available at:

- Swagger UI: http://localhost:8004/docs
- ReDoc: http://localhost:8004/redoc


### 6.3 Running unit tests


```bash
pip install -r requirements.txt -r requirements-test.txt

PYTHONPATH=. pytest
```
