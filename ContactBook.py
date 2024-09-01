import tkinter as tk
from tkinter import messagebox


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # Frames
        self.frame1 = tk.Frame(self.root, bg="deeppink1")
        self.frame1.pack(fill="both", expand=True)

        self.frame2 = tk.Frame(self.root, bg="deeppink1")
        self.frame2.pack(fill="both", expand=True)

        self.frame3 = tk.Frame(self.root, bg="deeppink1")
        self.frame3.pack(fill="both", expand=True)

        # Labels and Entries
        tk.Label(self.frame1, text="Name:", bg="deeppink1").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame1, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Phone:", bg="deeppink1").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.frame1, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Email:", bg="deeppink1").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.frame1, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Address:", bg="deeppink1").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.frame1, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.frame2, text="Add Contact", command=self.add_contact, width=15).grid(row=0, column=0, padx=5,
                                                                                            pady=5)
        tk.Button(self.frame2, text="Search Contact", command=self.search_contact, width=15).grid(row=0, column=1,
                                                                                                  padx=5, pady=5)
        tk.Button(self.frame2, text="Update Contact", command=self.update_contact, width=15).grid(row=0, column=2,
                                                                                                  padx=5, pady=5)
        tk.Button(self.frame2, text="Delete Contact", command=self.delete_contact, width=15).grid(row=0, column=3,
                                                                                                  padx=5, pady=5)

        # Text box
        self.text_box = tk.Text(self.frame3, width=50, height=10)
        self.text_box.pack(fill="both", expand=True)

        self.display_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if self.validate_name(name) and self.validate_phone(phone) and email and address:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            messagebox.showinfo("Success", "Contact added successfully")
            self.clear_entries()
            self.display_contacts()
        else:
            messagebox.showerror("Error", "Please fill all fields correctly")

    def display_contacts(self):
        self.text_box.delete(1.0, tk.END)
        for name, details in self.contacts.items():
            self.text_box.insert(tk.END,
                                 f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n\n")

    def search_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name:
            if name in self.contacts:
                details = self.contacts[name]
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END,
                                     f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            else:
                messagebox.showerror("Error", "Contact not found")
        elif phone:
            for name, details in self.contacts.items():
                if details['phone'] == phone:
                    self.text_box.delete(1.0, tk.END)
                    self.text_box.insert(tk.END,
                                         f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
                    return
            messagebox.showerror("Error", "Contact not found")
        else:
            messagebox.showerror("Error", "Please enter a name or phone number to search")

    def update_contact(self):
            name = self.name_entry.get()
            if name:
                if name in self.contacts:
                    phone = self.phone_entry.get()
                    email = self.email_entry.get()
                    address = self.address_entry.get()

                    if self.validate_phone(phone) and email and address:
                        self.contacts[name] = {
                            "phone": phone,
                            "email": email,
                            "address": address
                        }
                        messagebox.showinfo("Success", "Contact updated successfully")
                        self.clear_entries()
                        self.display_contacts()
                    else:
                        messagebox.showerror("Error", "Please fill all fields correctly")
                else:
                    messagebox.showerror("Error", "Contact not found")
            else:
                messagebox.showerror("Error", "Please enter a name to update")

    def delete_contact(self):
            name = self.name_entry.get()
            if name:
                if name in self.contacts:
                    del self.contacts[name]
                    messagebox.showinfo("Success", "Contact deleted successfully")
                    self.clear_entries()
                    self.display_contacts()
                else:
                    messagebox.showerror("Error", "Contact not found")
            else:
                messagebox.showerror("Error", "Please enter a name to delete")

    def clear_entries(self):
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)

    def validate_name(self, name):
            if name.isalpha():
                return True
            else:
                messagebox.showerror("Error", "Name should contain only alphabets")
                return False

    def validate_phone(self, phone):
            if phone.isdigit() and len(phone) == 10:
                return True
            else:
                messagebox.showerror("Error", "Phone number should contain only 10 digits")
                return False

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()