import unittest
from unittest.mock import MagicMock
import tkinter as tk
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui import ContactManagerUI

class TestContactManagerUI(unittest.TestCase):
    def setUp(self):
        # Create a mock database manager
        self.mock_db = MagicMock()
        self.mock_db.get_all_contacts.return_value = [
            ("Mock Name", "Mock Address", "Mock Gender", "12345")
        ]
        
        # Create a hidden Tk root
        self.root = tk.Tk()
        # Hide the window during tests
        self.root.withdraw()
        
        self.ui = ContactManagerUI(self.root, self.mock_db)

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        # Verify that get_all_contacts was called during init via load_contacts
        self.mock_db.get_all_contacts.assert_called()
        
        # Verify treeview contains the mock contact
        children = self.ui.tree.get_children()
        self.assertEqual(len(children), 1)
        item_values = self.ui.tree.item(children[0], 'values')
        # values are returned as strings or ints depending on Tkinter version, 
        # but usually strings from tree.item
        self.assertEqual(item_values[0], "Mock Name")
        self.assertEqual(item_values[3], "12345")

    def test_add_contact_success(self):
        # Set input values
        self.ui.name_input.set("New Contact")
        self.ui.addr_input.set("New Addr")
        self.ui.gender_input.set("New Gender")
        self.ui.phone_input.set("9999")
        
        # Simulate add button click
        self.ui.add_contact()
        
        # Verify DB add_contact was called with correct args
        self.mock_db.add_contact.assert_called_with("New Contact", "New Addr", "New Gender", "9999")
        
        # Verify inputs are cleared
        self.assertEqual(self.ui.name_input.get(), "")
        self.assertEqual(self.ui.phone_input.get(), "")

if __name__ == '__main__':
    unittest.main()
