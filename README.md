# Calendar Event Generator

## Overview

This is a Python project that generates `.ics` calendar files, which can be imported into any calendar application (compatible with macOS, Windows, iOS, Android, and Google Calendar). The script allows you to define multiple events, including recurring and one-time events, and automatically creates an `.ics` file containing these events.

### Key Features:
- Supports **yearly**, **monthly**, **weekly**, and **daily** recurring events.
- Automatically handles **default start and end times** if they are not provided.
- Simple and user-friendly customization: You only need to modify the `events` list in the script.

## Requirements

To run this project, you'll need to install the required Python dependencies. The dependencies are listed in the `requirements.txt` file, and the primary library used is:

- `ics` (for creating `.ics` calendar files)

## Installation

1. **Clone or download the repository**:
   Download the project files to your local machine.

2. **Install dependencies**:
   Open a terminal or command prompt, navigate to the folder containing the project files, and run the following command to install the required dependencies:

   ```bash
   pip install -r requirements.txt

	3.	Run the script:
To generate the .ics file, execute the script by running:

python main.py

This will create an .ics file with your events inside the output folder.

Usage

Step 1: Edit the events list

The only part of the script you should modify is the events list. This is where you define the events that you want to add to your calendar. Each event in the list is a dictionary with the following fields:

{
    "name": "Event Name",           # (Required) The name or title of the event.
    "day": 15,                      # (Required) The day of the event.
    "month": 8,                     # (Required) The month of the event.
    "year": 2024,                   # (Required) The year of the event.
    "start_time": "14:00",          # (Optional) The start time of the event in HH:MM format. Defaults to "09:00" if not provided.
    "end_time": "15:00",            # (Optional) The end time of the event in HH:MM format. Defaults to "12:00" if not provided.
    "recurrence": "YEARLY"          # (Optional) Recurrence rule: can be 'YEARLY', 'MONTHLY', 'WEEKLY', 'DAILY', or None for no recurrence.
}

Step 2: Add or Modify Events

	•	To add new events: Simply add new event dictionaries to the events list.
	•	To modify existing events: You can edit the existing dictionaries in the events list by changing the values for name, day, month, year, start_time, end_time, or recurrence.
	•	Do not modify the rest of the code: The script handles all the logic of generating the .ics file. You only need to edit the events list.

Example of Adding Events:

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

Step 3: Run the Script

Once you’ve edited the events list to include your desired events, run the script:

python main.py

Step 4: Output

The script will generate an .ics file containing your events and save it to the output folder. The output file will be named Add_to_calendar.ics. You can then open or import this file into your preferred calendar application.

File Structure

Here is the structure of the project:

calendar-event-generator/
│
├── main.py               # The main Python script to generate the .ics file
├── requirements.txt      # The file containing the required Python libraries
├── README.md             # This readme file
└── output/               # Folder where the .ics file will be saved

How the Script Works:

	•	Start and End Times: If you don’t provide a start_time or end_time, the script will default to 09:00 and 12:00, respectively.
	•	Recurrence: If you don’t specify a recurrence, the event will be a one-time event. Valid recurrence options include YEARLY, MONTHLY, WEEKLY, and DAILY.
	•	Event Name: Every event must have a name, day, month, and year. These are mandatory.

Important:

	•	Do not modify anything outside the events list. The rest of the code handles all the necessary logic for generating the .ics file and should not be changed.
	•	Only modify the events list to add, remove, or edit events.

License

This project is open-source and available under the MIT License.

---

### Summary of Changes:
1. The output file is now specified to be saved in the `output` folder.
2. Detailed explanations were added about how to edit the `events` list and what users should not modify (i.e., the code outside of the events list).
3. Clearer installation, usage, and structure explanations were provided to ensure that everything is easy to understand and follow.

You can now copy this entire `README.md` into your project’s readme file and it will guide users through the process clearly and effectively. Let me know if you need further refinements!