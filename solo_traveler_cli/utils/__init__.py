import os
import json
from pathlib import Path

BASE_DIR = Path.home() / ".solo_traveler_cli"
BASE_DIR.mkdir(parents=True, exist_ok=True)

def get_data_file(filename: str) -> Path:
    """Returns the full path to a data file inside the CLI's base storage directory."""
    return BASE_DIR / filename

def load_json(filename: str):
    """Loads JSON data from the user's data directory."""
    path = get_data_file(filename)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_json(filename: str, data):
    """Saves JSON data to the user's data directory."""
    path = get_data_file(filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)