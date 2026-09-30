import tkinter as tk
from modules.trip import TripModule
from modules.budget import BudgetModule
from modules.itinerary import ItineraryModule
from modules.storage import Storage

class TravelPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Planner")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)

        self.storage = Storage()
        self.trip = TripModule(self.root, self.storage)
        self.budget = BudgetModule(self.root, self.storage)
        self.itinerary = ItineraryModule(self.root, self.storage)

        self.create_ui()

    def create_ui(self):
        title = tk.Label(
            self.root,
            text="✈ Travel Planner",
            font=("Arial", 24, "bold"),
            pady=15
        )
        title.pack()

        subtitle = tk.Label(
            self.root,
            text="Simple Trip, Budget and Itinerary Manager",
            font=("Arial", 11)
        )
        subtitle.pack(pady=(0, 15))

        notebook = tk.Frame(self.root)
        notebook.pack(fill="both", expand=True, padx=20, pady=10)

        self.trip.create_tab(notebook)
        self.budget.create_tab(notebook)
        self.itinerary.create_tab(notebook)

        bottom = tk.Frame(self.root)
        bottom.pack(fill="x", padx=20, pady=10)

        tk.Button(
            bottom,
            text="Clear All Data",
            command=self.clear_data,
            bg="#d9534f",
            fg="white",
            padx=15
        ).pack(side="right")

    def clear_data(self):
        self.storage.clear()
        self.trip.refresh()
        self.budget.refresh()
        self.itinerary.refresh()

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelPlanner(root)
    root.mainloop()
