import unittest
import sqlite3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db_manager = DatabaseManager(':memory:')

    def tearDown(self):
        self.db_manager.close()

    def test_create_table(self):
        self.db_manager.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'")
        result = self.db_manager.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 'contacts')

    def test_add_contact_valid(self):
        self.db_manager.add_contact("John Doe", "123 Main St", "Male", "555-1234")
        self.db_manager.cursor.execute("SELECT * FROM contacts")
        result = self.db_manager.cursor.fetchall()
        self.assertEqual(len(result), 1)

    def test_add_contact_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            self.db_manager.add_contact("", "123 Main St", "Male", "555-1234")
        self.assertIn('name', context.exception.args[0])

        with self.assertRaises(ValueError) as context:
            self.db_manager.add_contact("A" * 51, "123 Main St", "Male", "555-1234")
        self.assertIn('name', context.exception.args[0])

    def test_add_contact_invalid_phone(self):
        with self.assertRaises(ValueError) as context:
            self.db_manager.add_contact("John", "123 Main St", "Male", "invalid-phone")
        self.assertIn('phone', context.exception.args[0])

        with self.assertRaises(ValueError) as context:
            self.db_manager.add_contact("John", "123 Main St", "Male", "1234567890123456")
        self.assertIn('phone', context.exception.args[0])

    def test_get_all_contacts(self):
        self.db_manager.add_contact("Alice", "Address A", "Female", "111")
        self.db_manager.add_contact("Bob", "Address B", "Male", "222")
        contacts = self.db_manager.get_all_contacts()
        self.assertEqual(len(contacts), 2)

    def test_delete_contact(self):
        self.db_manager.add_contact("Charlie", "Address C", "Male", "333")
        self.db_manager.delete_contact("Charlie", "333")
        contacts = self.db_manager.get_all_contacts()
        self.assertEqual(len(contacts), 0)

if __name__ == '__main__':
    unittest.main()
