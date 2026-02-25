"""Tests for load_scripts function."""

from check_runner import load_scripts


def test_load_scripts_from_directory(tmp_path):
    check_dir = tmp_path / "my_check"
    check_dir.mkdir()
    (check_dir / "01_first.sql").write_text("SELECT 1")
    (check_dir / "02_second.sql").write_text("SELECT 2")

    scripts = load_scripts(tmp_path)

    assert len(scripts) == 1
    assert scripts[0][0] == "my_check"
    assert len(scripts[0][1]) == 2
    assert scripts[0][1][0] == ("01_first.sql", "SELECT 1")
    assert scripts[0][1][1] == ("02_second.sql", "SELECT 2")


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

    scripts = load_scripts(tmp_path)

    assert [name for name, _ in scripts] == ["a_check", "m_check", "z_check"]


def test_load_scripts_empty_directory(tmp_path):
    scripts = load_scripts(tmp_path)
    assert scripts == []


def test_load_scripts_ignores_non_sql_files(tmp_path):
    check_dir = tmp_path / "my_check"
    check_dir.mkdir()
    (check_dir / "check.sql").write_text("SELECT 1")
    (check_dir / "readme.txt").write_text("not a sql file")

    scripts = load_scripts(tmp_path)

    assert len(scripts) == 1
    assert len(scripts[0][1]) == 1
    assert scripts[0][1][0][0] == "check.sql"


def test_load_scripts_stages_sorted(tmp_path):
    check_dir = tmp_path / "my_check"
    check_dir.mkdir()
    (check_dir / "03_third.sql").write_text("SELECT 3")
    (check_dir / "01_first.sql").write_text("SELECT 1")
    (check_dir / "02_second.sql").write_text("SELECT 2")

    scripts = load_scripts(tmp_path)

    assert len(scripts) == 1
    stage_names = [name for name, _ in scripts[0][1]]
    assert stage_names == ["01_first.sql", "02_second.sql", "03_third.sql"]
