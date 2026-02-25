"""Tests for load_scripts function."""

from check_runner import load_scripts


def test_load_scripts_from_directory(tmp_path):
    script1 = tmp_path / "001_check.sql"
    script1.write_text("SELECT 1")
    script2 = tmp_path / "002_check.sql"
    script2.write_text("SELECT 2")

    scripts = load_scripts(tmp_path)

    assert len(scripts) == 2
    assert scripts[0] == ("001_check.sql", "SELECT 1")
    assert scripts[1] == ("002_check.sql", "SELECT 2")


def test_load_scripts_sorted(tmp_path):
    script_z = tmp_path / "z_check.sql"
    script_z.write_text("SELECT z")
    script_a = tmp_path / "a_check.sql"
    script_a.write_text("SELECT a")
    script_m = tmp_path / "m_check.sql"
    script_m.write_text("SELECT m")

    scripts = load_scripts(tmp_path)

    assert [name for name, _ in scripts] == ["a_check.sql", "m_check.sql", "z_check.sql"]


def test_load_scripts_empty_directory(tmp_path):
    scripts = load_scripts(tmp_path)
    assert scripts == []


def test_load_scripts_ignores_non_sql_files(tmp_path):
    script = tmp_path / "check.sql"
    script.write_text("SELECT 1")
    other = tmp_path / "readme.txt"
    other.write_text("not a sql file")

    scripts = load_scripts(tmp_path)

    assert len(scripts) == 1
    assert scripts[0][0] == "check.sql"
