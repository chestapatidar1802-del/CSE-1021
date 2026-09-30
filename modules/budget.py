import tkinter as tk
from tkinter import messagebox

class BudgetModule:
    def __init__(self, parent, storage):
        self.parent = parent
        self.storage = storage
        self.listbox = None
        self.name_entry = None
        self.amount_entry = None
        self.total_label = None
        self.remaining_label = None

    def create_tab(self, notebook):
        self.frame = tk.LabelFrame(notebook, text="Budget Planner", padx=20, pady=20)
        self.frame.pack(fill="x", pady=5)

        tk.Label(self.frame, text="Expense Name").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame, text="Amount (₹)").grid(row=1, column=0, sticky="w")
        self.amount_entry = tk.Entry(self.frame, width=30)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(
            self.frame,
            text="Add Expense",
            command=self.add_expense,
            bg="#1769aa",
            fg="white"
        ).grid(row=2, column=1, pady=10)

        self.listbox = tk.Listbox(self.frame, width=65, height=7)
        self.listbox.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(
            self.frame,
            text="Delete Selected",
            command=self.delete_expense,
            bg="#d9534f",
            fg="white"
        ).grid(row=4, column=1, pady=5)

        self.total_label = tk.Label(self.frame, text="Total Spent: ₹0")
        self.total_label.grid(row=5, column=0, sticky="w", pady=5)

        self.remaining_label = tk.Label(self.frame, text="Remaining: ₹0")
        self.remaining_label.grid(row=6, column=0, sticky="w", pady=5)

        self.refresh()

    def add_expense(self):
        name = self.name_entry.get().strip()
        amount_text = self.amount_entry.get().strip()

        if not name or not amount_text:
            messagebox.showerror("Error", "Enter expense name and amount.")
            return

        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid positive amount.")
            return

        data = self.storage.load()
        data["expenses"].append({"name": name, "amount": amount})
        self.storage.save(data)

        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.refresh()

    def delete_expense(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Select", "Select an expense first.")
            return

        index = selected[0]
        data = self.storage.load()
        del data["expenses"][index]
        self.storage.save(data)
        self.refresh()

    def refresh(self):
        if self.listbox is None:
            return

        self.listbox.delete(0, tk.END)
        data = self.storage.load()
        expenses = data.get("expenses", [])

        total = 0
        for expense in expenses:
            total += expense["amount"]
            self.listbox.insert(
                tk.END,
                f'{expense["name"]}  -  ₹{expense["amount"]:.2f}'
            )

        budget = float(data.get("trip", {}).get("budget", 0) or 0)
        remaining = budget - total

        self.total_label.config(text=f"Total Spent: ₹{total:.2f}")
        self.remaining_label.config(text=f"Remaining: ₹{remaining:.2f}")
