# Travel Planner Documentation

## Architecture
User
  |
  v
Tkinter GUI
  |
  +--> Trip Module
  |
  +--> Budget Module
  |
  +--> Itinerary Module
  |
  v
Storage Module
  |
  v
travel_data.json

## Workflow
1. Open the application.
2. Enter trip details.
3. Validate and save trip.
4. Add travel expenses.
5. Application calculates total spent and remaining budget.
6. Add itinerary activities with date and time.
7. Delete incorrect records when required.
8. Data remains saved locally.

## Non-Functional Requirements
1. Usability - simple graphical interface.
2. Performance - lightweight local application.
3. Reliability - validation and JSON storage.
4. Maintainability - separate Python modules.
5. Error Handling - invalid input displays messages.

## Meaningful Files
- main.py
- trip.py
- budget.py
- itinerary.py
- storage.py
- README.md
- statement.md
- documentation.md

## Testing Approach
Functional testing is used for form validation, calculations, CRUD-like add/delete operations and data persistence.
