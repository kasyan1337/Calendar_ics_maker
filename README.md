Calendar Event Generator

# Overview

This is a Python project that generates .ics calendar files, which can be imported into any calendar application (compatible with macOS, Windows, iOS, Android, and Google Calendar). The script allows you to define multiple events, including recurring and one-time events, and automatically creates an .ics file containing these events.

## Key Features

	•	Supports yearly, monthly, weekly, and daily recurring events.
	•	Customizable alerts in ISO 8601 format, including countdown alerts (e.g., PT10S to PT1S).
	•	Automatically handles default start and end times if they are not provided.
	•	Easy event customization: Simply modify the events list in the script.

## Requirements

To run this project, install the required Python dependencies listed in requirements.txt:
```bash
pip install -r requirements.txt
``` 

## Usage

Step 1: Edit the Events List

Customize the events list to define the events you want in your calendar. Each event in the list is a dictionary with the following fields:
``` 
{
    "name": "Event Name",           # (Required) Title of the event.
    "day": 15,                      # (Required) Day of the event.
    "month": 8,                     # (Required) Month of the event.
    "year": 2024,                   # (Required) Year of the event.
    "start_time": "14:00",          # (Optional) Start time in HH:MM format. Defaults to "09:00" if omitted.
    "end_time": "15:00",            # (Optional) End time in HH:MM format. Defaults to "12:00" if omitted.
    "recurrence": "YEARLY",         # (Optional) Recurrence rule: 'YEARLY', 'MONTHLY', 'WEEKLY', 'DAILY', or None for one-time events.
    "is_all_day": False,            # (Optional) If True, sets event as all-day. Defaults to False.
    "alerts": ["PT0M", "P1D"]       # (Optional) List of ISO 8601 durations for reminders (e.g., "PT5M" for 5 mins before).
}
``` 
Step 2: Add or Modify Events

	•	To add events: Simply add new event dictionaries to the events list.
	•	To modify events: Update values in existing dictionaries (like name, day, month, etc.).

Example Event Entries:
``` 
events = [
    {
        "name": "Project Deadline",
        "day": 10,
        "month": 12,
        "year": 2024,
        "start_time": "09:00",
        "end_time": "11:00",
        "recurrence": None  # This is a one-time event
    },
    {
        "name": "Weekly Staff Meeting",
        "day": 1,
        "month": 11,
        "year": 2024,
        "start_time": "14:00",
        "end_time": "15:00",
        "recurrence": "WEEKLY"  # This event recurs weekly
    },
    {
        "name": "John's Birthday",
        "day": 13,
        "month": 5,
        "year": 2024,
        "recurrence": "YEARLY"  # This event recurs yearly
    }
]
``` 
Step 3: Run the Script

After customizing the events list, generate the .ics file by running:

python main.py

Step 4: Import the Generated .ics File

The script generates a file named Add_to_calendar.ics in the output folder. You can import this file into any compatible calendar application.

## File Structure

calendar-event-generator/
│
├── main.py               # Main Python script to generate the .ics file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── output/               # Folder where the .ics file is saved

## Event Configuration Details

	1.	Start and End Times: Defaults to 09:00 and 12:00, respectively, if not provided.
	2.	Recurrence: Events without a specified recurrence are treated as one-time events. Valid recurrence options include:
	•	YEARLY
	•	MONTHLY
	•	WEEKLY
	•	DAILY
	3.	Alerts: Supports ISO 8601 duration formats such as PT10S, PT5M, P1D, etc., for customizable reminders.
	4.	Countdown Alerts: To enable countdown alerts from 10 seconds before the event, set the alerts field using a lambda function:
``` 
"alerts": lambda: [f"PT{seconds}S" for seconds in range(10, 0, -1)]
``` 

## Important Notes

	•	Only edit the events list: All customizations should be made in the events list. Do not modify code outside this list.
	•	Avoid Duplicate Alerts: The script automatically removes duplicate alerts for each event.
