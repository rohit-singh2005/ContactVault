import tkinter as tk
from tkinter import ttk, messagebox
import re

class ContactManagerUI:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        
        self.root.title("Contact Management System")

        self.name_input = tk.StringVar()
        self.addr_input = tk.StringVar()
        self.gender_input = tk.StringVar()
        self.phone_input = tk.StringVar()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Helper method to create bordered entry
        def create_bordered_entry(row, label_text, text_var):
            tk.Label(self.frame, text=label_text).grid(row=row, column=0, sticky='e', padx=5, pady=2)
            
            border_frame = tk.Frame(self.frame, bg="gray", padx=1, pady=1)
            border_frame.grid(row=row, column=1, pady=2, sticky='w')
            
            entry = tk.Entry(border_frame, textvariable=text_var, relief=tk.FLAT)
            entry.pack(fill=tk.BOTH, expand=True)
            
            err_label = tk.Label(self.frame, text="", fg="red")
            err_label.grid(row=row+1, column=1, sticky='w')
            
            return border_frame, entry, err_label

        # Name
        self.name_frame, self.name_entry, self.name_err_label = create_bordered_entry(0, "Name", self.name_input)
        # Address
        self.addr_frame, self.addr_entry, self.addr_err_label = create_bordered_entry(2, "Address", self.addr_input)
        # Gender
        self.gender_frame, self.gender_entry, self.gender_err_label = create_bordered_entry(4, "Gender", self.gender_input)
        # Phone
        self.phone_frame, self.phone_entry, self.phone_err_label = create_bordered_entry(6, "Phone", self.phone_input)

        tk.Button(self.frame, text="Add Contact", command=self.add_contact).grid(row=8, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(root, columns=('Name', 'Address', 'Gender', 'Phone'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Address', text='Address')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Phone', text='Phone')
        self.tree.pack()

        self.tree.bind('<Double-1>', self.remove_contact)

        self.load_contacts()

    def clear_errors(self):
        self.name_frame.config(bg="gray")
        self.addr_frame.config(bg="gray")
        self.gender_frame.config(bg="gray")
        self.phone_frame.config(bg="gray")
        
        self.name_err_label.config(text="")
        self.addr_err_label.config(text="")
        self.gender_err_label.config(text="")
        self.phone_err_label.config(text="")

    def show_error(self, field, msg):
        if field == 'name':
            self.name_frame.config(bg="red")
            self.name_err_label.config(text=msg)
        elif field == 'address':
            self.addr_frame.config(bg="red")
            self.addr_err_label.config(text=msg)
        elif field == 'gender':
            self.gender_frame.config(bg="red")
            self.gender_err_label.config(text=msg)
        elif field == 'phone':
            self.phone_frame.config(bg="red")
            self.phone_err_label.config(text=msg)

    def validate_inputs_client_side(self, name, address, gender, phone):
        errors = {}
        if not name or len(name) < 1 or len(name) > 50:
            errors['name'] = "Name must be between 1 and 50 characters."
        if address and len(address) > 100:
            errors['address'] = "Address must be under 100 characters."
        if gender and len(gender) > 20:
            errors['gender'] = "Gender must be under 20 characters."
        if not phone or not re.match(r'^[\d\-+]+$', phone) or len(phone) > 15:
            errors['phone'] = "Phone must be valid digits/symbols (+, -) and max 15 chars."
        return errors

    def add_contact(self):
        self.clear_errors()
        name = self.name_input.get()
        address = self.addr_input.get()
        gender = self.gender_input.get()
        phone = self.phone_input.get()
        
        client_errors = self.validate_inputs_client_side(name, address, gender, phone)
        if client_errors:
            for field, msg in client_errors.items():
                self.show_error(field, msg)
            return

        try:
            self.db_manager.add_contact(name, address, gender, phone)
            self.load_contacts()
            self.name_input.set('')
            self.addr_input.set('')
            self.gender_input.set('')
            self.phone_input.set('')
        except ValueError as e:
            server_errors = e.args[0]
            if isinstance(server_errors, dict):
                for field, msg in server_errors.items():
                    self.show_error(field, msg)
            else:
                messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add contact: {e}")

    def load_contacts(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for contact in self.db_manager.get_all_contacts():
            self.tree.insert('', tk.END, values=contact)

    def remove_contact(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            self.db_manager.delete_contact(values[0], values[3])
            self.load_contacts()
