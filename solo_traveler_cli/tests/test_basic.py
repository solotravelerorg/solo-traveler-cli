import subprocess

def test_cli_help():
    """Test that the CLI returns help info"""
    result = subprocess.run(["python", "-m", "solo_traveler_cli.main", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Solo Traveler CLI" in result.stdout
    assert "trip" in result.stdout
    assert "journal" in result.stdout
    assert "packing" in result.stdout
    assert "expense" in result.stdout
