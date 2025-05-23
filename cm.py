import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ContactManager:
    def __init__(self, root):
        self.db = sqlite3.connect('contacts.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            gender TEXT,
            phone TEXT)''')
        self.db.commit()

        self.root = root
        self.root.title("Contact Management System")

        self.name_input = tk.StringVar()
        self.addr_input = tk.StringVar()
        self.gender_input = tk.StringVar()
        self.phone_input = tk.StringVar()

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Name").grid(row=0, column=0)
        tk.Entry(frame, textvariable=self.name_input).grid(row=0, column=1)

        tk.Label(frame, text="Address").grid(row=1, column=0)
        tk.Entry(frame, textvariable=self.addr_input).grid(row=1, column=1)

        tk.Label(frame, text="Gender").grid(row=2, column=0)
        tk.Entry(frame, textvariable=self.gender_input).grid(row=2, column=1)

        tk.Label(frame, text="Phone").grid(row=3, column=0)
        tk.Entry(frame, textvariable=self.phone_input).grid(row=3, column=1)

        tk.Button(frame, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=5)

        self.tree = ttk.Treeview(root, columns=('Name', 'Address', 'Gender', 'Phone'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Address', text='Address')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Phone', text='Phone')
        self.tree.pack()

        self.tree.bind('<Double-1>', self.remove_contact)

        self.load_contacts()

    def add_contact(self):
        name = self.name_input.get()
        address = self.addr_input.get()
        gender = self.gender_input.get()
        phone = self.phone_input.get()
        if name and phone:
            self.cursor.execute("INSERT INTO contacts (name, address, gender, phone) VALUES (?, ?, ?, ?)", 
                                (name, address, gender, phone))
            self.db.commit()
            self.load_contacts()
            self.name_input.set('')
            self.addr_input.set('')
            self.gender_input.set('')
            self.phone_input.set('')
        else:
            messagebox.showerror("Error", "Name and phone are required.")

    def load_contacts(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for contact in self.cursor.execute("SELECT name, address, gender, phone FROM contacts"):
            self.tree.insert('', tk.END, values=contact)

    def remove_contact(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            self.cursor.execute("DELETE FROM contacts WHERE name=? AND phone=?", (values[0], values[3]))
            self.db.commit()
            self.load_contacts()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
