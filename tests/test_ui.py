import unittest
from unittest.mock import MagicMock
import tkinter as tk
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui import ContactManagerUI

class TestContactManagerUI(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.get_all_contacts.return_value = [
            ("Mock Name", "Mock Address", "Mock Gender", "12345")
        ]
        
        self.root = tk.Tk()
        self.root.withdraw()
        
        self.ui = ContactManagerUI(self.root, self.mock_db)

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        self.mock_db.get_all_contacts.assert_called()
        children = self.ui.tree.get_children()
        self.assertEqual(len(children), 1)

    def test_add_contact_success(self):
        self.ui.name_input.set("New Contact")
        self.ui.addr_input.set("New Addr")
        self.ui.gender_input.set("New Gender")
        self.ui.phone_input.set("9999")
        
        self.ui.add_contact()
        self.mock_db.add_contact.assert_called_with("New Contact", "New Addr", "New Gender", "9999")
        self.assertEqual(self.ui.name_input.get(), "")
        self.assertEqual(self.ui.name_err_label.cget("text"), "")
        self.assertEqual(self.ui.name_frame.cget("bg"), "gray")

    def test_add_contact_client_validation_failure(self):
        self.ui.name_input.set("")
        self.ui.phone_input.set("invalid phone")
        
        self.ui.add_contact()
        
        self.mock_db.add_contact.assert_not_called()
        self.assertEqual(self.ui.name_err_label.cget("text"), "Name must be between 1 and 50 characters.")
        self.assertEqual(self.ui.name_frame.cget("bg"), "red")
        self.assertEqual(self.ui.phone_err_label.cget("text"), "Phone must be valid digits/symbols (+, -) and max 15 chars.")
        self.assertEqual(self.ui.phone_frame.cget("bg"), "red")

if __name__ == '__main__':
    unittest.main()
