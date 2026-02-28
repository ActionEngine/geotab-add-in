"""Tests for main function."""

import logging
from contextlib import contextmanager
from unittest.mock import MagicMock, patch

import pytest

from check_runner import main


# Script folders referenced by CHECKS (check name -> folder name)
# Both road-counter checks use the same "road-counter" script folder
REQUIRED_SCRIPT_FOLDERS = ["road-counter"]


def setup_check_dirs(tmp_path):
    """Helper to create the required check directory structures."""
    for folder_name in REQUIRED_SCRIPT_FOLDERS:
        check_dir = tmp_path / folder_name
        check_dir.mkdir()
        (check_dir / "01_stage.sql").write_text("SELECT 1")
    return tmp_path
