FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir psycopg2-binary==2.9.10

COPY check-runner/check_runner.py .

COPY check-runner/scripts/ ./scripts/

# Default: run once. Set CHECK_INTERVAL_SECONDS to run in a loop.
CMD ["python", "check_runner.py"]
