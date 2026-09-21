# ContactVault

ContactVault is a desktop contact management application built with Python. It provides a graphical interface for adding, viewing, and deleting contact records.

The application stores contact data in a local SQLite database, so no external database server is required.

## Features

* Add a contact with name, address, gender, and phone number.
* View saved contacts in a table.
* Delete a contact by double-clicking its record.
* Validate required fields before saving a contact.
* Store contact data in a local SQLite database.
* Automatically create the database and contacts table when the application starts.

## Tech Stack

* **Python** — Application logic
* **Tkinter** — Graphical user interface
* **ttk.Treeview** — Contact table
* **SQLite3** — Local database
* **SQL** — Database queries and data management

## Application Structure

```text
User
  |
  v
Tkinter GUI
  |
  v
ContactManager
  |
  +-- Add Contact
  |
  +-- View Contacts
  |
  +-- Delete Contact
  |
  v
SQLite Database
  |
  v
contacts.db
```

## Database

The application creates a SQLite database named:

```text
contacts.db
```

It contains a `contacts` table with the following fields:

| Field     | Type    | Description          |
| --------- | ------- | -------------------- |
| `id`      | INTEGER | Primary key          |
| `name`    | TEXT    | Contact name         |
| `address` | TEXT    | Contact address      |
| `gender`  | TEXT    | Contact gender       |
| `phone`   | TEXT    | Contact phone number |

The table is created automatically if it does not already exist.

## Requirements

* Python 3.x
* Tkinter
* SQLite3

Tkinter and SQLite3 are part of the standard Python library. No external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/rohit-si
```
