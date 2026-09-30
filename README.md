# Travel Planner - Python

## Overview
Travel Planner is a simple Python desktop application for planning trips.

## Main Functional Modules
1. Trip Details Module
2. Budget Planner Module
3. Itinerary Planner Module

## Technologies
- Python 3
- Tkinter
- JSON
- Object-Oriented Programming
- File Handling

## Requirements
Python 3.x is required. Tkinter is included with most standard Python installations.

## How to Run

Open the project folder in VS Code and run:

```bash
python main.py
```

If `python` does not work on Windows, use:

```bash
py main.py
```

## Features
- Save destination and trip dates
- Set traveller count and budget
- Add/delete expenses
- Calculate total spent and remaining budget
- Add/delete itinerary activities
- Validate dates, time and numeric values
- Automatically save data in `travel_data.json`

## Testing
Test:
- Empty form validation
- Invalid dates
- End date before start date
- Invalid budget
- Add and delete expenses
- Add and delete itinerary plans
- Data persistence after closing and reopening

## Future Enhancements
- Weather API
- Google Maps
- Hotel search
- Login system
- Database support
