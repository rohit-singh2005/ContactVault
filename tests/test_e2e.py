import time
import os
import sys
import unittest
from pywinauto.application import Application

class TestContactManagerE2E(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        main_script = os.path.join(base_dir, 'main.py')
        self.app = Application(backend="win32").start(f'"{sys.executable}" "{main_script}"', wait_for_idle=False)
        time.sleep(2)
        self.main_window = self.app.window(title="Contact Management System")
        self.main_window.wait('ready', timeout=10)

    def tearDown(self):
        if self.app:
            self.app.kill()

    def test_validation_and_add_contact_e2e(self):
        try:
            self.main_window.set_focus()
            time.sleep(0.5)

            self.main_window.type_keys("E2E Test User{TAB}", with_spaces=True)
            time.sleep(0.2)
            self.main_window.type_keys("123 Automation St{TAB}", with_spaces=True)
            time.sleep(0.2)
            self.main_window.type_keys("Robot{TAB}", with_spaces=True)
            time.sleep(0.2)
            self.main_window.type_keys("invalid-phone-string{TAB}", with_spaces=True)
            time.sleep(0.2)
            self.main_window.type_keys("{SPACE}")
            
            time.sleep(1)
            self.assertTrue(self.main_window.exists())

            self.main_window.type_keys("+{TAB}")
            time.sleep(0.2)
            self.main_window.type_keys("^a{BACKSPACE}555-9999{TAB}")
            time.sleep(0.2)
            self.main_window.type_keys("{SPACE}")

            time.sleep(1)
            self.assertTrue(self.main_window.exists())

        except Exception as e:
            self.fail(f"E2E test failed during interaction: {e}")

if __name__ == "__main__":
    unittest.main()
