import json
from pathlib import Path

class Storage:
    def __init__(self):
        self.file = Path("travel_data.json")

    def load(self):
        if not self.file.exists():
            return {"trip": {}, "expenses": [], "plans": []}

        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {"trip": {}, "expenses": [], "plans": []}

    def save(self, data):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def clear(self):
        data = {"trip": {}, "expenses": [], "plans": []}
        self.save(data)
