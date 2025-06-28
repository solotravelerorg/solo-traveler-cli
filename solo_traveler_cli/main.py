import typer
from solo_traveler_cli.commands import trip, journal, packing, expense

app = typer.Typer(help="Solo Traveler CLI — Plan trips, track expenses, pack smart, and journal on the go.")

# Add subcommands
app.add_typer(trip.app, name="trip", help="Manage trips")
app.add_typer(journal.app, name="journal", help="Write and read travel journals")
app.add_typer(packing.app, name="packing", help="Create and manage packing lists")
app.add_typer(expense.app, name="expense", help="Track your travel expenses and budgets")

if __name__ == "__main__":
    app()