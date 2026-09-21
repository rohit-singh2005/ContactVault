# ContactVault

ContactVault is a robust desktop contact management application built with Python. It provides a graphical interface for adding, viewing, and deleting contact records.

The application stores contact data in a local SQLite database, so no external database server is required. Recently refactored into a modular architecture, ContactVault now boasts strict client and server-side input validation and comprehensive test coverage.

## Features

* Add a contact with name, address, gender, and phone number.
* View saved contacts in a table.
* Delete a contact by double-clicking its record.
* **Strict Input Validation**: Fields are validated client-side and server-side. Invalid inputs result in a red highlighted border and inline error messages.
* **SQL Injection Prevention**: Uses parameterized queries and regex formatting for safety.
* Store contact data in a local SQLite database.
* Automatically create the database and contacts table when the application starts.

## Tech Stack

* **Python** — Application logic
* **Tkinter** — Graphical user interface
* **ttk.Treeview** — Contact table
* **SQLite3** — Local database
* **Unittest & Pywinauto** — Deep unit and end-to-end testing

## Application Structure

The monolithic structure has been broken out into manageable modules:
- `main.py`: Entry point for the application.
- `ui.py`: Manages Tkinter UI, visual validation feedback, and event handlers.
- `database.py`: Manages SQLite connections, query parametrization, and data rule enforcement.
- `tests/`: Contains comprehensive automated test suites.

## Database

The application creates a SQLite database named: `contacts.db`

It contains a `contacts` table with the following fields:

| Field     | Type    | Description          | Validation Rules |
| --------- | ------- | -------------------- | ---------------- |
| `id`      | INTEGER | Primary key          | Auto-generated   |
| `name`    | TEXT    | Contact name         | 1-50 characters  |
| `address` | TEXT    | Contact address      | Max 100 characters |
| `gender`  | TEXT    | Contact gender       | Max 20 characters  |
| `phone`   | TEXT    | Contact phone number | Digits/+, max 15 chars |

## Test Coverage

ContactVault features deep testing using Python's `unittest` framework and `pywinauto`.

**Test Suites included:**
- `test_database.py`: Tests SQLite insertions, deletions, and constraint violations (Server-side validation).
- `test_ui.py`: Tests UI states, visual validation boundaries (red borders), and mock database connections.
- `test_e2e.py`: End-to-end tests driving the actual UI with physical keyboard simulations to ensure everything flows correctly.

### Running Tests

We have included a beautiful script to summarize your test results! Run the following command in your terminal:

```bash
python run_tests.py
```

This will automatically discover all tests, run them, and provide a summary of how many tests passed, failed, or errored out.

## Requirements

* Python 3.x
* Tkinter (Usually included with Python)
* `pywinauto` (For End-to-End tests)

To install the E2E dependencies, run:
```bash
pip install pywinauto
```

## Installation

Clone the repository and run:

```bash
python main.py
```
