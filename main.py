from datetime import datetime, timedelta

import pytz
from ics import Calendar, Event
from ics.grammar.parse import ContentLine  # Import ContentLine

# Define Bratislava timezone
bratislava_tz = pytz.timezone("Europe/Bratislava")

# Create a calendar
c = Calendar()

events_example = [{
    "name": "Someone's Birthday",  # Mandatory: Name of the event, a descriptive title for the event.

    "day": 13,  # Mandatory: Day of the event (1-31 depending on the month)
    "month": 5,  # Mandatory: Month of the event (1-12)
    "year": 2024,  # Mandatory: Year of the event (4-digit format, e.g., 2024)

    "start_time": "09:00",  # Optional: Event start time in HH:MM format, defaults to "09:00" if not specified
    "end_time": "12:00",  # Optional: Event end time in HH:MM format, defaults to "12:00" if not specified

    "recurrence": "YEARLY",  # Optional: Event recurrence frequency.
    # Options:
    #   - "YEARLY": Repeats every year on the same date.
    #   - "MONTHLY": Repeats every month on the same day.
    #   - "WEEKLY": Repeats every week on the same day.
    #   - "DAILY": Repeats every day.
    #   - None: No recurrence (default if not specified).

    "is_all_day": False,  # Optional: If True, sets the event as an all-day event without a specific start or end time.
    # Defaults to False. If set to True, "start_time" and "end_time" are ignored.

    "alerts": ["PT0M", "PT5M", "PT30M", "P1D"]  # Optional: List of reminders for the event in ISO 8601 duration format.
    # Examples:
    #   - "PT0M": Alert at the exact time of the event.
    #   - "PT5M": Alert 5 minutes before the event.
    #   - "PT30M": Alert 30 minutes before the event.
    #   - "P1D": Alert 1 day before the event.
    # You can add multiple alerts as needed.
}]

# Events list
events = [
    {"name": "Test1", "day": 29, "month": 10, "year": 2024, "start_time": "08:00", "end_time": "11:00",
     "recurrence": "YEARLY", "alerts": ["PT0M", "P1D"]},
    {"name": "Test2_fullday", "day": 30, "month": 10, "year": 2024, "recurrence": "MONTHLY", "alerts": ["PT0M"],
     "is_all_day": True},
    # Add more events as needed
]


# Function to add recurrence rules based on the user's input
def add_recurrence_rule(event, e):
    recurrence = event.get("recurrence")
    if recurrence:
        e.extra.append(ContentLine(name='RRULE', params={}, value=f'FREQ={recurrence}'))


# Function to add alerts based on specified times
def add_alerts(event, e):
    alerts = event.get("alerts", [])
    for alert in alerts:
        # Calculate alert time based on the event start time
        if alert.startswith("P") and alert.endswith("D"):  # Handle days format like "P1D"
            days = int(alert[1:-1])  # Extract number of days
            alert_time = e.begin - timedelta(days=days)
        elif alert.startswith("PT") and alert.endswith("M"):  # Handle minutes format like "PT5M"
            minutes = int(alert[2:-1])  # Extract number of minutes
            alert_time = e.begin - timedelta(minutes=minutes)
        else:
            alert_time = e.begin  # Default to event start time if format is unrecognized

        # Add the alert as a description for now since ics library doesn't support native VALARM
        e.description = (e.description or "") + f"\nAlert set for {alert_time}"


# Iterate over the events and add them to the calendar
for event in events:
    e = Event()
    e.name = event["name"]

    # Handle all-day events
    if event.get("is_all_day", False):
        # Set the date without time or timezone for all-day events
        e.begin = datetime(event["year"], event["month"], event["day"])
        e.make_all_day()
    else:
        # Provide default start and end times if not present
        start_time = event.get("start_time", "09:00")
        end_time = event.get("end_time", "12:00")

        # Format the start and end times with the given year, month, and day in the Bratislava timezone
        start_datetime = datetime.strptime(f'{event["year"]}-{event["month"]:02d}-{event["day"]:02d} {start_time}',
                                           "%Y-%m-%d %H:%M")
        end_datetime = datetime.strptime(f'{event["year"]}-{event["month"]:02d}-{event["day"]:02d} {end_time}',
                                         "%Y-%m-%d %H:%M")

        # Set timezone to Bratislava
        e.begin = bratislava_tz.localize(start_datetime)
        e.end = bratislava_tz.localize(end_datetime)

    # Add recurrence if specified
    add_recurrence_rule(event, e)

    # Add alerts if specified
    add_alerts(event, e)

    # Add the event to the calendar
    c.events.add(e)

# Save to a .ics file
with open('output/Add_to_calendar.ics', 'w') as my_file:
    my_file.write(c.serialize())

print("Calendar saved with events and alerts.")
