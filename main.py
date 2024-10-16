from ics import Calendar, Event

# Create a calendar
c = Calendar()

# List of events with detailed parameters (name, day, month, year, start_time, end_time, recurrence)
events_example = [
    {
        "name": "Someone's Birthday",
        "day": 13,
        "month": 5,
        "year": 2024,
        "start_time": "09:00",  # Optional, defaults to 09:00
        "end_time": "12:00",  # Optional, defaults to 12:00
        "recurrence": "YEARLY"  # Recurrence can be 'YEARLY', 'MONTHLY', 'WEEKLY', 'DAILY', or None
    },
    {
        "name": "Monthly Team Meeting",
        "day": 1,
        "month": 6,
        "year": 2024,
        "start_time": "10:00",
        "end_time": "11:00",
        "recurrence": "MONTHLY"
    },
    {
        "name": "Weekly Yoga Class",
        "day": 4,
        "month": 7,
        "year": 2024,
        "start_time": "17:00",
        "end_time": "18:00",
        "recurrence": "WEEKLY"
    },
    {
        "name": "One-time Appointment",
        "day": 15,
        "month": 8,
        "year": 2024,
        "start_time": "14:00",
        "end_time": "15:00",
        "recurrence": None
    },
    # Add more events as needed
]

events = [

]


# Function to add recurrence rules based on the user's input
def add_recurrence_rule(event, e):
    recurrence = event.get("recurrence")  # Safely get recurrence or None if missing
    if recurrence == "YEARLY":
        e.make_all_day()  # Optional: assume it's an all-day event for yearly recurrences
        e.repeat = "YEARLY"
    elif recurrence == "MONTHLY":
        e.repeat = "MONTHLY"
    elif recurrence == "WEEKLY":
        e.repeat = "WEEKLY"
    elif recurrence == "DAILY":
        e.repeat = "DAILY"
    else:
        pass  # No recurrence for one-time events


# Iterate over the events and add them to the calendar
for event in events:
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

    # Add the event to the calendar
    c.events.add(e)

# Save to a .ics file
with open('output/Add_to_calendar.ics', 'w') as my_file:
    my_file.writelines(c)
