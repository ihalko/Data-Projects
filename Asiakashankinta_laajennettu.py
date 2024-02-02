from pandasgui import show
import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog

class ContactManager:
    def __init__(self):
        self.customer_df = pd.DataFrame(columns=["Name", "Company", "Contact Type", "Email", "Phone",
                                                  "Title", "Answered", "Notes", "Date Contacted"])

    def on_add_contact(self):
        name = self.name_entry.get()
        company = self.company_entry.get()
        contact_type = self.contact_type_var.get().lower()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        title = self.title_entry.get()
        answered = self.answered_var.get()
        notes = self.notes_entry.get()
        date_contacted = self.date_entry.get()

        new_contact = pd.DataFrame({
            "Name": [name],
            "Company": [company],
            "Contact Type": [contact_type],
            "Email": [email],
            "Phone": [phone],
            "Title": [title],
            "Answered": [answered.lower()],
            "Notes": [notes],
            "Date Contacted": [date_contacted]
        })

        self.customer_df = pd.concat([self.customer_df, new_contact], ignore_index=True)

        messagebox.showinfo("Contact Added", f"Contact added for {name}.")

        self.clear_entry_fields()

    def on_print_contacts(self):
        if self.customer_df.empty:
            messagebox.showinfo("No Contacts", "No contacts available.")
        else:
            show(self.customer_df, settings={'block': True})

    def export_to_csv(self):
        if self.customer_df.empty:
            messagebox.showinfo("No Data", "No data to export.")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                self.customer_df.to_csv(file_path, index=False)
                messagebox.showinfo("Export Successful", f"Data exported to {file_path}.")

    def clear_entry_fields(self):
        self.name_entry.delete(0, tk.END)
        self.company_entry.delete(0, tk.END)
        self.contact_type_var.set("Call")
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.answered_var.set("False")
        self.notes_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def add_contact_gui(self):
        root = tk.Tk()
        root.title("Contact Manager")

        tk.Label(root, text="Customer Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Company Name:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Contact Type:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Email:").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(root, text="Phone:").grid(row=4, column=0, padx=10, pady=5)
        tk.Label(root, text="Title:").grid(row=5, column=0, padx=10, pady=5)
        tk.Label(root, text="Answered:").grid(row=6, column=0, padx=10, pady=5)
        tk.Label(root, text="Notes:").grid(row=7, column=0, padx=10, pady=5)
        tk.Label(root, text="Date Contacted:").grid(row=8, column=0, padx=10, pady=5)

        self.name_entry = tk.Entry(root)
        self.company_entry = tk.Entry(root)
        self.contact_type_var = tk.StringVar(value="Call")
        self.email_entry = tk.Entry(root)
        self.phone_entry = tk.Entry(root)
        self.title_entry = tk.Entry(root)
        self.answered_var = tk.StringVar(value="False")
        self.notes_entry = tk.Entry(root)
        self.date_entry = tk.Entry(root)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.company_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.OptionMenu(root, self.contact_type_var, "Call", "Email").grid(row=2, column=1, padx=10, pady=5)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)
        self.phone_entry.grid(row=4, column=1, padx=10, pady=5)
        self.title_entry.grid(row=5, column=1, padx=10, pady=5)
        tk.OptionMenu(root, self.answered_var, "True", "False").grid(row=6, column=1, padx=10, pady=5)
        self.notes_entry.grid(row=7, column=1, padx=10, pady=5)
        self.date_entry.grid(row=8, column=1, padx=10, pady=5)

        tk.Button(root, text="Add Contact", command=self.on_add_contact, height=2).grid(row=9, column=0, columnspan=3, pady=10)
        tk.Button(root, text="Print Contacts", command=self.on_print_contacts, height=2).grid(row=10, column=0, columnspan=3, pady=10)
        tk.Button(root, text="Export to CSV", command=self.export_to_csv, height=2).grid(row=11, column=0, columnspan=3, pady=10)

        root.mainloop()

# Sample usage
if __name__ == "__main__":
    manager = ContactManager()
    manager.add_contact_gui()
