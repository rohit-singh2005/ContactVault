import sqlite3
import re

class DatabaseManager:
    def __init__(self, db_name='contacts.db'):
        self.db_name = db_name
        self.db = sqlite3.connect(self.db_name)
        self.cursor = self.db.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            gender TEXT,
            phone TEXT)''')
        self.db.commit()

    def validate_contact(self, name, address, gender, phone):
        errors = {}
        if not name or len(name) < 1 or len(name) > 50:
            errors['name'] = "Name must be between 1 and 50 characters."
        if address and len(address) > 100:
            errors['address'] = "Address must be under 100 characters."
        if gender and len(gender) > 20:
            errors['gender'] = "Gender must be under 20 characters."
        if not phone or not re.match(r'^[\d\-+]+$', phone) or len(phone) > 15:
            errors['phone'] = "Phone must be valid digits/symbols (+, -) and max 15 chars."
        
        if errors:
            raise ValueError(errors)

    def add_contact(self, name, address, gender, phone):
        self.validate_contact(name, address, gender, phone)
        self.cursor.execute("INSERT INTO contacts (name, address, gender, phone) VALUES (?, ?, ?, ?)", 
                            (name, address, gender, phone))
        self.db.commit()

    def get_all_contacts(self):
        self.cursor.execute("SELECT name, address, gender, phone FROM contacts")
        return self.cursor.fetchall()

    def delete_contact(self, name, phone):
        self.cursor.execute("DELETE FROM contacts WHERE name=? AND phone=?", (name, phone))
        self.db.commit()

    def close(self):
        self.db.close()
