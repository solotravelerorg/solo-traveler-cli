# Solo Traveler CLI

A command-line tool to help solo travelers plan trips, track expenses, manage packing lists, and write travel journals — all from the comfort of your terminal.

## Features

- 🗺️ **Trip Management** – Add and list upcoming trips
- 📓 **Travel Journals** – Write and read entries for each trip
- 🧳 **Packing Lists** – Create and manage per-trip packing checklists
- 💰 **Expense Tracking** – Set budgets and log travel expenses

## Installation

Clone the repo and install locally:

```bash
git clone https://github.com/solotravelerorg/solo-traveler-cli.git
cd solo-traveler-cli
pip install .
```

Make sure you have Python 3.7 or later installed.

## Usage

Run the CLI with:

```bash
solo --help
```

### Trips

```bash
solo trip add "Tokyo" "2025-10-01" "2025-10-10"
solo trip list
```

### Journals

```bash
solo journal new "Tokyo"
solo journal write "Tokyo" "Visited Senso-ji and ate ramen in Asakusa."
solo journal read "Tokyo"
```

### Packing

```bash
solo packing new "Tokyo"
solo packing add-item "Tokyo" "Passport"
solo packing list "Tokyo"
solo packing check "Tokyo" 1
```

### Expenses

```bash
solo expense set-budget "Tokyo" 1500
solo expense add "Tokyo" 45 food "Dinner at sushi bar"
solo expense summary "Tokyo"
```

## Data Storage

All data is saved locally in:

```bash
~/.solo_traveler_cli/
```

Each module (trips, journals, packing, expenses) maintains its own files.

## Testing

To run tests:

```bash
pytest tests/
```

## License

[MIT License](LICENSE)

## Contributing

Pull requests and suggestions are welcome. For major changes, please open an issue first to discuss what you'd like to change.

**Solo Traveler CLI** is built with ❤️ to help solo travelers plan smarter and travel lighter.
