import typer
from solo_traveler_cli.utils import load_json, save_json
from datetime import datetime

app = typer.Typer()
TRIP_FILE = "trips.json"

@app.command()
def add(destination: str, start_date: str, end_date: str):
    """
    Add a new trip with destination, start date, and end date.
    """
    trips = load_json(TRIP_FILE)

    trip_id = str(len(trips) + 1)
    trips[trip_id] = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "created_at": datetime.now().isoformat()
    }

    save_json(TRIP_FILE, trips)
    typer.echo(f"✅ Trip to {destination} from {start_date} to {end_date} saved.")

@app.command("list")
def list_trips():
    """
    List all saved trips.
    """
    trips = load_json(TRIP_FILE)
    if not trips:
        typer.echo("No trips found.")
        return

    typer.echo("📍 Saved Trips:")
    for trip_id, trip in trips.items():
        typer.echo(f"[{trip_id}] {trip['destination']} ({trip['start_date']} → {trip['end_date']})")
