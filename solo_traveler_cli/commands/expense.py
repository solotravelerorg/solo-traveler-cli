import typer
from solo_traveler_cli.utils import load_json, save_json

app = typer.Typer()
EXPENSE_PREFIX = "expenses_"  # Each trip's expense data is stored as expenses_<trip>.json

@app.command("set-budget")
def set_budget(trip_name: str, amount: float):
    """
    Set a total travel budget for a trip.
    """
    filename = f"{EXPENSE_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    data = load_json(filename)

    data["budget"] = amount
    data["expenses"] = data.get("expenses", [])

    save_json(filename, data)
    typer.echo(f"💰 Budget of ${amount:.2f} set for '{trip_name}'.")

@app.command("add")
def add_expense(trip_name: str, amount: float, category: str = "misc", note: str = ""):
    """
    Add a travel expense to a trip.
    """
    filename = f"{EXPENSE_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    data = load_json(filename)

    if "budget" not in data:
        typer.echo("⚠️ No budget set yet. Run `solo expense set-budget` first.")
        return

    data.setdefault("expenses", []).append({
        "amount": amount,
        "category": category,
        "note": note
    })

    save_json(filename, data)
    typer.echo(f"🧾 Added ${amount:.2f} to '{trip_name}' under '{category}'.")

@app.command("summary")
def show_summary(trip_name: str):
    """
    Show the budget summary and expenses breakdown for a trip.
    """
    filename = f"{EXPENSE_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    data = load_json(filename)

    if not data or "budget" not in data:
        typer.echo("⚠️ No data found. Set a budget and add expenses first.")
        return

    total_spent = sum(e["amount"] for e in data.get("expenses", []))
    remaining = data["budget"] - total_spent

    typer.echo(f"💼 Expense Summary for '{trip_name}':")
    typer.echo(f"  Budget:   ${data['budget']:.2f}")
    typer.echo(f"  Spent:    ${total_spent:.2f}")
    typer.echo(f"  Remaining:${remaining:.2f}")

    typer.echo("\n📊 Breakdown:")
    for i, e in enumerate(data["expenses"], 1):
        note = f" — {e['note']}" if e['note'] else ""
        typer.echo(f"{i}. ${e['amount']:.2f} | {e['category']}{note}")