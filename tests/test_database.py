import unittest
import sqlite3
import os
import sys

# Add parent directory to path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        # Use an in-memory database for testing
        self.db_manager = DatabaseManager(':memory:')

    def tearDown(self):
        self.db_manager.close()

    def test_create_table(self):
        # Check if table exists
        self.db_manager.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'")
        result = self.db_manager.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 'contacts')

    def test_add_contact(self):
        self.db_manager.add_contact("John Doe", "123 Main St", "Male", "555-1234")
        
        self.db_manager.cursor.execute("SELECT * FROM contacts")
        result = self.db_manager.cursor.fetchall()
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "John Doe")
        self.assertEqual(result[0][2], "123 Main St")
        self.assertEqual(result[0][3], "Male")
        self.assertEqual(result[0][4], "555-1234")

    def test_get_all_contacts(self):
        self.db_manager.add_contact("Alice", "Address A", "Female", "111")
        self.db_manager.add_contact("Bob", "Address B", "Male", "222")
        
        contacts = self.db_manager.get_all_contacts()
        self.assertEqual(len(contacts), 2)
        
        self.assertEqual(contacts[0], ("Alice", "Address A", "Female", "111"))
        self.assertEqual(contacts[1], ("Bob", "Address B", "Male", "222"))

    def test_delete_contact(self):
        self.db_manager.add_contact("Charlie", "Address C", "Male", "333")
        self.db_manager.add_contact("Diana", "Address D", "Female", "444")
        
        # Delete Charlie
        self.db_manager.delete_contact("Charlie", "333")
        
        contacts = self.db_manager.get_all_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0][0], "Diana")

if __name__ == '__main__':
    unittest.main()
