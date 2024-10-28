from ics import Calendar, Event
from datetime import datetime, timedelta

# Create a calendar
c = Calendar()

# Example list of events with detailed parameters (name, day, month, year, start_time, end_time, recurrence)
events_example = [
    {
        "name": "Someone's Birthday",
        "day": 13,
        "month": 5,
        "year": 2024,
        "start_time": "09:00",
        "end_time": "12:00",
        "recurrence": "YEARLY",
        "alerts": ["PT0M", "PT5M", "PT30M", "P1D"]  # Reminders at event time, 5 min, 30 min, and 1 day before
    },
    {
        "name": "Monthly Team Meeting",
        "day": 1,
        "month": 6,
        "year": 2024,
        "start_time": "10:00",
        "end_time": "11:00",
        "recurrence": "MONTHLY",
        "alerts": ["PT15M"]  # Remind 15 minutes before
    },
    {
        "name": "Weekly Yoga Class",
        "day": 4,
        "month": 7,
        "year": 2024,
        "start_time": "17:00",
        "end_time": "18:00",
        "recurrence": "WEEKLY",
        "alerts": ["PT10M"]  # Remind 10 minutes before
    },
    {
        "name": "One-time Appointment",
        "day": 15,
        "month": 8,
        "year": 2024,
        "start_time": "14:00",
        "end_time": "15:00",
        "recurrence": None,
        "alerts": ["P1D"]  # Remind 1 day before
    },
]

# Additional events
events = [
    {"name": "Milan", "day": 27, "month": 11, "year": 2024, "recurrence": "YEARLY", "alerts": ["PT0M", "P1D"]},
    {"name": "Milada", "day": 29, "month": 12, "year": 2024, "recurrence": "YEARLY", "alerts": ["PT0M"]},
    # Add more events as needed
]

# Function to add recurrence rules based on the user's input
def add_recurrence_rule(event, e):
    recurrence = event.get("recurrence")
    if recurrence == "YEARLY":
        e.make_all_day()
        e.repeat = "YEARLY"
    elif recurrence == "MONTHLY":
        e.repeat = "MONTHLY"
    elif recurrence == "WEEKLY":
        e.repeat = "WEEKLY"
    elif recurrence == "DAILY":
        e.repeat = "DAILY"

# Function to add alerts based on specified times
def add_alerts(event, e):
    alerts = event.get("alerts", [])
    for alert in alerts:
        # Calculate alert time based on the event start time
        if alert.startswith("P"):
            alert_time = datetime.strptime(e.begin, "%Y-%m-%d %H:%M") - timedelta(days=int(alert[1]))
        elif alert.startswith("PT"):
            minutes = int(alert[2:-1])
            alert_time = datetime.strptime(e.begin, "%Y-%m-%d %H:%M") - timedelta(minutes=minutes)
        else:
            alert_time = e.begin

        # Add the alert as a description for now since ics library doesn't support native VALARM
        e.description = (e.description or "") + f"\nAlert set for {alert_time}"

# Iterate over the events and add them to the calendar
for event in events_example + events:
    e = Event()
    e.name = event["name"]

    # Provide default start and end times if not present
    start_time = event.get("start_time", "09:00")
    end_time = event.get("end_time", "12:00")

    # Format the start and end times with the given year, month, and day
    start_datetime = f'{event["year"]}-{event["month"]:02d}-{event["day"]:02d} {start_time}'
    end_datetime = f'{event["year"]}-{event["month"]:02d}-{event["day"]:02d} {end_time}'

    e.begin = start_datetime
    e.end = end_datetime

    # Add recurrence if specified
    add_recurrence_rule(event, e)

    # Add alerts if specified
    add_alerts(event, e)

    # Add the event to the calendar
    c.events.add(e)

# Save to a .ics file
with open('output/Add_to_calendar.ics', 'w') as my_file:
    my_file.writelines(c)

print("Calendar saved with events and alerts.")