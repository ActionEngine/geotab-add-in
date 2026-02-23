# GeoTab downloader

This tool downloads the GeoTab entities and saves them locally as csv files.

Currently supported entities:
- Device
- StatusData
- LogRecord
- Diagnostic

## Usage

Install uv following insructions from their site: https://docs.astral.sh/uv/getting-started/installation/

Run this script: `uv run geotab-downloader -u <username> -p <password> -d <geotab-database>`

This will download all of the supported entities that exist in the database

## Dependency management

- add new dependency: `uv add package`
- add new dev dependency `uv add --dev package`
- refresh venv and lockfile (uv.lock) after adding dependency `uv sync`

## Running tests locally

- uv run pytest

## Configuring other project tools

- edit pyproject.toml

## Why uv?

- Much better performance. Can save minutes during CI/CD builds
- Guaranteed Reproducibility: Uses uv.lock for deterministic, cross-platform builds across dev, CI, and production.
- Robust Resolution: A modern resolver that handles complex dependency conflicts better than legacy tools.
- Native Python Management: Automatically installs and manages any Python version—no more manual installs or Docker overhead for local dev.
