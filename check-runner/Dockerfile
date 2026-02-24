FROM python:3.13-slim

WORKDIR /app

# psycopg2 dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir psycopg2-binary==2.9.10

# Copy runner script from check-runner subdirectory
COPY check-runner/check_runner.py .

# Copy SQL scripts from check-runner subdirectory
COPY check-runner/check-scripts/ ./check-scripts/

CMD ["python", "check_runner.py"]
