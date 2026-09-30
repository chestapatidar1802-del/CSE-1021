import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TripModule:
    def __init__(self, parent, storage):
        self.parent = parent
        self.storage = storage
        self.entries = {}

    def create_tab(self, notebook):
        self.frame = tk.LabelFrame(notebook, text="Trip Details", padx=20, pady=20)
        self.frame.pack(fill="x", pady=5)

        fields = [
            ("Destination", "destination"),
            ("Start Date (DD-MM-YYYY)", "start"),
            ("End Date (DD-MM-YYYY)", "end"),
            ("Travellers", "travellers"),
            ("Budget (₹)", "budget")
        ]

        for row, (label, key) in enumerate(fields):
            tk.Label(self.frame, text=label).grid(row=row, column=0, sticky="w", pady=6)
            entry = tk.Entry(self.frame, width=35)
            entry.grid(row=row, column=1, padx=15, pady=6)
            self.entries[key] = entry

        tk.Button(
            self.frame,
            text="Save Trip",
            command=self.save_trip,
            bg="#1769aa",
            fg="white",
            width=15
        ).grid(row=5, column=1, pady=15)

        self.load_trip()

    def save_trip(self):
        destination = self.entries["destination"].get().strip()
        start = self.entries["start"].get().strip()
        end = self.entries["end"].get().strip()
        travellers = self.entries["travellers"].get().strip()
        budget = self.entries["budget"].get().strip()

        if not destination or not start or not end or not travellers or not budget:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        try:
            start_date = datetime.strptime(start, "%d-%m-%Y")
            end_date = datetime.strptime(end, "%d-%m-%Y")
            travellers = int(travellers)
            budget = float(budget)

            if end_date < start_date:
                raise ValueError("End date cannot be before start date.")
            if travellers < 1:
                raise ValueError("Travellers must be at least 1.")
            if budget < 0:
                raise ValueError("Budget cannot be negative.")

        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error))
            return

        data = self.storage.load()
        data["trip"] = {
            "destination": destination,
            "start": start,
            "end": end,
            "travellers": travellers,
            "budget": budget
        }
        self.storage.save(data)

        messagebox.showinfo("Success", "Trip saved successfully!")

    def load_trip(self):
        trip = self.storage.load().get("trip", {})
        for key, value in trip.items():
            if key in self.entries:
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, str(value))

    def refresh(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.load_trip()
