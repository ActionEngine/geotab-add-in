"""Smoke tests for SQL scripts - validates SQL by running in a rolled-back transaction."""

import os
from pathlib import Path

import psycopg2
import pytest

from check_runner import load_scripts


def _get_scripts():
    """Get all SQL scripts for parametrization."""
    scripts_dir = Path("check-scripts")
    return load_scripts(scripts_dir)


@pytest.mark.smoke
@pytest.mark.parametrize("name,sql", _get_scripts())
def test_sql_script_valid(name, sql):
    """Validate a SQL script by running it in a transaction that gets rolled back.
    
    This allows testing INSERT/UPDATE statements without actually modifying the database.
    """
    database_url = os.environ["DATABASE_URL"]
    
    with psycopg2.connect(database_url) as conn:
        conn.rollback()
        
        with conn.cursor() as cur:
            cur.execute(sql)
        
        conn.rollback()
