import typer
from solo_traveler_cli.utils import load_json, save_json

app = typer.Typer()
PACKING_PREFIX = "packing_"  # Each packing list is stored as packing_<trip>.json

@app.command("new")
def new_list(trip_name: str):
    """
    Create a new packing list for a trip.
    """
    filename = f"{PACKING_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    existing = load_json(filename)
    if existing:
        typer.echo(f"⚠️ A packing list for '{trip_name}' already exists.")
    else:
        save_json(filename, [])
        typer.echo(f"🧳 New packing list created for '{trip_name}'.")

@app.command("add-item")
def add_item(trip_name: str, item: str):
    """
    Add an item to the packing list.
    """
    filename = f"{PACKING_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    packing_list = load_json(filename)

    if not isinstance(packing_list, list):
        typer.echo("⚠️ Packing list not found. Run `solo packing new` first.")
        return

    packing_list.append({"item": item, "packed": False})
    save_json(filename, packing_list)
    typer.echo(f"✅ Added '{item}' to the packing list for '{trip_name}'.")

@app.command("list")
def list_items(trip_name: str):
    """
    Show all items in the packing list.
    """
    filename = f"{PACKING_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    packing_list = load_json(filename)

    if not packing_list:
        typer.echo("⚠️ No packing list found or list is empty.")
        return

    typer.echo(f"🧳 Packing list for '{trip_name}':")
    for i, entry in enumerate(packing_list, 1):
        status = "✅" if entry["packed"] else "⬜"
        typer.echo(f"{i}. {status} {entry['item']}")

@app.command("check")
def mark_item(trip_name: str, item_number: int):
    """
    Mark an item in the packing list as packed.
    """
    filename = f"{PACKING_PREFIX}{trip_name.lower().replace(' ', '_')}.json"
    packing_list = load_json(filename)

    if not packing_list or item_number < 1 or item_number > len(packing_list):
        typer.echo("⚠️ Invalid item number or packing list missing.")
        return

    packing_list[item_number - 1]["packed"] = True
    save_json(filename, packing_list)
    typer.echo(f"✅ Marked '{packing_list[item_number - 1]['item']}' as packed.")