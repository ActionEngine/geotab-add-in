"""Tests for load_scripts function."""

import pytest

from check_runner import load_scripts


def test_load_scripts_from_directory(tmp_path):
    check_dir = tmp_path / "my_check"
    check_dir.mkdir()
    (check_dir / "01_first.sql").write_text("SELECT 1")
    (check_dir / "02_second.sql").write_text("SELECT 2")

    checks = {"my_check": {}}
    scripts = load_scripts(tmp_path, checks)

    assert len(scripts) == 1
    assert scripts[0][0] == "my_check"
    assert len(scripts[0][1]) == 2
    assert scripts[0][1][0] == ("01_first.sql", "SELECT 1")
    assert scripts[0][1][1] == ("02_second.sql", "SELECT 2")
    assert scripts[0][2] == {}


def test_load_scripts_sorted(tmp_path):
    z_dir = tmp_path / "z_check"
    z_dir.mkdir()
    (z_dir / "01_z.sql").write_text("SELECT z")

    a_dir = tmp_path / "a_check"
    a_dir.mkdir()
    (a_dir / "01_a.sql").write_text("SELECT a")

    m_dir = tmp_path / "m_check"
    m_dir.mkdir()
    (m_dir / "01_m.sql").write_text("SELECT m")

    checks = {"a_check": {}, "m_check": {}, "z_check": {}}
    scripts = load_scripts(tmp_path, checks)

    assert [name for name, _, _ in scripts] == ["a_check", "m_check", "z_check"]


def test_load_scripts_empty_contexts(tmp_path):
    checks = {}
    scripts = load_scripts(tmp_path, checks)
    assert scripts == []


def test_load_scripts_missing_directory_raises(tmp_path):
    checks = {"missing_check": {}}

    with pytest.raises(FileNotFoundError, match="Check directory not found"):
        load_scripts(tmp_path, checks)


def test_load_scripts_empty_directory_raises(tmp_path):
    check_dir = tmp_path / "my_check"
    check_dir.mkdir()
    checks = {"my_check": {}}

    with pytest.raises(FileNotFoundError, match="No SQL files found"):
        load_scripts(tmp_path, checks)


def test_load_scripts_ignores_non_sql_files(tmp_path):
    check_dir = tmp_path / "my_check"
    check_dir.mkdir()
    (check_dir / "check.sql").write_text("SELECT 1")
    (check_dir / "readme.txt").write_text("not a sql file")

    checks = {"my_check": {}}
    scripts = load_scripts(tmp_path, checks)

    assert len(scripts) == 1
    assert len(scripts[0][1]) == 1
    assert scripts[0][1][0][0] == "check.sql"
    assert scripts[0][2] == {}


def test_load_scripts_stages_sorted(tmp_path):
    check_dir = tmp_path / "my_check"
    check_dir.mkdir()
    (check_dir / "03_third.sql").write_text("SELECT 3")
    (check_dir / "01_first.sql").write_text("SELECT 1")
    (check_dir / "02_second.sql").write_text("SELECT 2")

    checks = {"my_check": {}}
    scripts = load_scripts(tmp_path, checks)

    assert len(scripts) == 1
    stage_names = [name for name, _ in scripts[0][1]]
    assert stage_names == ["01_first.sql", "02_second.sql", "03_third.sql"]
    assert scripts[0][2] == {}


def test_load_scripts_partial_match_raises(tmp_path):
    """Test that directories not in contexts are ignored, but missing contexts raise."""
    check_dir = tmp_path / "existing_check"
    check_dir.mkdir()
    (check_dir / "01_stage.sql").write_text("SELECT 1")

    checks = {"existing_check": {}, "missing_check": {}}

    with pytest.raises(FileNotFoundError, match="Check directory not found.*missing_check"):
        load_scripts(tmp_path, checks)


def test_load_scripts_with_script_folder(tmp_path):
    """Test that script_folder can point to a different directory than check name."""
    check_dir = tmp_path / "shared_scripts"
    check_dir.mkdir()
    (check_dir / "01_stage.sql").write_text("SELECT 1")

    checks = {"my_check": {"script_folder": "shared_scripts", "params": {"key": "value"}}}
    scripts = load_scripts(tmp_path, checks)

    assert len(scripts) == 1
    assert scripts[0][0] == "my_check"  # check name preserved
    assert len(scripts[0][1]) == 1
    assert scripts[0][2] == {"key": "value"}


def test_load_scripts_multiple_checks_same_folder(tmp_path):
    """Test multiple checks reusing the same script folder."""
    check_dir = tmp_path / "shared_scripts"
    check_dir.mkdir()
    (check_dir / "01_stage.sql").write_text("SELECT 1")

    checks = {
        "check_a": {"script_folder": "shared_scripts", "params": {"param": "a"}},
        "check_b": {"script_folder": "shared_scripts", "params": {"param": "b"}},
    }
    scripts = load_scripts(tmp_path, checks)

    assert len(scripts) == 2
    assert scripts[0][0] == "check_a"
    assert scripts[1][0] == "check_b"
    # Both should have same stages from shared folder
    assert len(scripts[0][1]) == 1
    assert len(scripts[1][1]) == 1
    # Each has its own params
    assert scripts[0][2] == {"param": "a"}
    assert scripts[1][2] == {"param": "b"}


def test_load_scripts_script_folder_not_found(tmp_path):
    """Test that missing script_folder raises error."""
    checks = {"my_check": {"script_folder": "missing_folder"}}

    with pytest.raises(FileNotFoundError, match="Check directory not found.*missing_folder"):
        load_scripts(tmp_path, checks)


def test_load_scripts_mixed_folders_and_script_folders(tmp_path):
    """Test mixing checks with and without script_folder."""
    # Regular check folder
    regular_dir = tmp_path / "regular_check"
    regular_dir.mkdir()
    (regular_dir / "01_stage.sql").write_text("SELECT 1")

    # Shared folder
    shared_dir = tmp_path / "shared_scripts"
    shared_dir.mkdir()
    (shared_dir / "01_stage.sql").write_text("SELECT 2")

    checks = {
        "regular_check": {},  # uses own folder
        "custom_check": {"script_folder": "shared_scripts"},  # uses shared
    }
    scripts = load_scripts(tmp_path, checks)

    assert len(scripts) == 2
    names = [name for name, _, _ in scripts]
    assert "regular_check" in names
    assert "custom_check" in names
    # regular_check has no params, custom_check has empty params
    regular = next(s for s in scripts if s[0] == "regular_check")
    custom = next(s for s in scripts if s[0] == "custom_check")
    assert regular[2] == {}
    assert custom[2] == {}
