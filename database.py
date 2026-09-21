import sqlite3

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

    def add_contact(self, name, address, gender, phone):
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
