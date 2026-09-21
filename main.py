import tkinter as tk
from database import DatabaseManager
from ui import ContactManagerUI

def main():
    root = tk.Tk()
    db_manager = DatabaseManager()
    app = ContactManagerUI(root, db_manager)
    
    def on_closing():
        db_manager.close()
        root.destroy()
        
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
