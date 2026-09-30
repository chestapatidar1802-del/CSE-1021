import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ItineraryModule:
    def __init__(self, parent, storage):
        self.parent = parent
        self.storage = storage
        self.listbox = None
        self.date_entry = None
        self.time_entry = None
        self.place_entry = None

    def create_tab(self, notebook):
        self.frame = tk.LabelFrame(notebook, text="Itinerary Planner", padx=20, pady=20)
        self.frame.pack(fill="x", pady=5)

        tk.Label(self.frame, text="Date (DD-MM-YYYY)").grid(row=0, column=0, sticky="w", pady=5)
        self.date_entry = tk.Entry(self.frame, width=25)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame, text="Time (HH:MM)").grid(row=1, column=0, sticky="w", pady=5)
        self.time_entry = tk.Entry(self.frame, width=25)
        self.time_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame, text="Place / Activity").grid(row=2, column=0, sticky="w", pady=5)
        self.place_entry = tk.Entry(self.frame, width=35)
        self.place_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(
            self.frame,
            text="Add Plan",
            command=self.add_plan,
            bg="#1769aa",
            fg="white"
        ).grid(row=3, column=1, pady=10)

        self.listbox = tk.Listbox(self.frame, width=75, height=8)
        self.listbox.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(
            self.frame,
            text="Delete Selected",
            command=self.delete_plan,
            bg="#d9534f",
            fg="white"
        ).grid(row=5, column=1, pady=5)

        self.refresh()

    def add_plan(self):
        date = self.date_entry.get().strip()
        time = self.time_entry.get().strip()
        place = self.place_entry.get().strip()

        if not date or not time or not place:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        try:
            datetime.strptime(date, "%d-%m-%Y")
            datetime.strptime(time, "%H:%M")
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Date must be DD-MM-YYYY and time must be HH:MM."
            )
            return

        data = self.storage.load()
        data["plans"].append({
            "date": date,
            "time": time,
            "place": place
        })

        data["plans"].sort(key=lambda x: (
            datetime.strptime(x["date"], "%d-%m-%Y"),
            datetime.strptime(x["time"], "%H:%M")
        ))

        self.storage.save(data)

        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.place_entry.delete(0, tk.END)
        self.refresh()

    def delete_plan(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Select", "Select an itinerary item first.")
            return

        index = selected[0]
        data = self.storage.load()
        del data["plans"][index]
        self.storage.save(data)
        self.refresh()

    def refresh(self):
        if self.listbox is None:
            return

        self.listbox.delete(0, tk.END)
        plans = self.storage.load().get("plans", [])

        for plan in plans:
            self.listbox.insert(
                tk.END,
                f'{plan["date"]} | {plan["time"]} | {plan["place"]}'
            )
