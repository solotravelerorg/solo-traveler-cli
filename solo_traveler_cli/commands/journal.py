import typer
from datetime import datetime
from solo_traveler_cli.utils import load_json, save_json

app = typer.Typer()
JOURNAL_PREFIX = "journal_"  # Each journal is stored as journal_<trip>.json

@app.command("new")
def new_journal(trip_name: str):
    """
    Start a new journal for a given trip.
    """
    filename = f"{JOURNAL_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    existing = load_json(filename)
    if existing:
        typer.echo(f"⚠️ Journal for '{trip_name}' already exists.")
    else:
        save_json(filename, [])
        typer.echo(f"📓 Created new journal for '{trip_name}'.")

@app.command("write")
def write_entry(trip_name: str, entry: str):
    """
    Write a dated journal entry for the specified trip.
    """
    filename = f"{JOURNAL_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    journal = load_json(filename)

    if not isinstance(journal, list):
        typer.echo("⚠️ No journal found. Please run `solo journal new` first.")
        return

    journal.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "entry": entry
    })

    save_json(filename, journal)
    typer.echo("✅ Entry saved.")

@app.command("read")
def read_journal(trip_name: str):
    """
    Read all journal entries for a given trip.
    """
    filename = f"{JOURNAL_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    journal = load_json(filename)

    if not journal:
        typer.echo("⚠️ No journal found or no entries yet.")
        return

    typer.echo(f"📓 Journal for '{trip_name}':")
    for i, entry in enumerate(journal, 1):
        typer.echo(f"{i}. [{entry['date']}] {entry['entry']}")