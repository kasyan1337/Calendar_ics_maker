from datetime import datetime, timedelta

from ics import Calendar, Event

# Create a calendar
c = Calendar()

# Example list of events with detailed parameters (name, day, month, year, start_time, end_time, recurrence)
events_example = [{
    "name": "Someone's Birthday",  # Mandatory: Name of the event
    "day": 13,  # Mandatory: Day of the event (1-31 depending on the month)
    "month": 5,  # Mandatory: Month of the event (1-12)
    "year": 2024,  # Mandatory: Year of the event (4-digit format, e.g., 2024)
    "start_time": "09:00",  # Optional: Event start time in HH:MM format, defaults to "09:00" if not specified
    "end_time": "12:00",  # Optional: Event end time in HH:MM format, defaults to "12:00" if not specified
    "recurrence": "YEARLY",
    # Optional: Event recurrence, options are 'YEARLY', 'MONTHLY', 'WEEKLY', 'DAILY', or None for no recurrence
    "alerts": ["PT0M", "PT5M", "PT30M", "P1D"]
    # Optional: List of reminders, formatted as ISO 8601 durations (e.g., "PT5M" for 5 min, "P1D" for 1 day)
}]

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
