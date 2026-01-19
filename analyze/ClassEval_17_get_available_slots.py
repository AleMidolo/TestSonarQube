def get_available_slots(self, date):
    """
    Get all available time slots on a given date.
    :param date: The date to get available time slots for,datetime.
    :return: A list of available time slots on the given date,list.
    >>> calendar = CalendarUtil()
    >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
    >>> calendar.get_available_slots(datetime(2023, 1, 1))
    [(datetime.datetime(2023, 1, 1, 23, 0), datetime.datetime(2023, 1, 2, 0, 0))]

    """
    from datetime import datetime, timedelta
    
    # Define the start and end of the day
    day_start = datetime(date.year, date.month, date.day, 0, 0)
    day_end = datetime(date.year, date.month, date.day, 0, 0) + timedelta(days=1)
    
    # Get all events on the given date
    events_on_date = []
    for event in self.events:
        event_start = event['start_time']
        event_end = event['end_time']
        
        # Check if event overlaps with the given date
        if event_start.date() == date.date() or event_end.date() == date.date() or \
           (event_start.date() < date.date() < event_end.date()):
            events_on_date.append(event)
    
    # Sort events by start time
    events_on_date.sort(key=lambda x: x['start_time'])
    
    # Find available slots
    available_slots = []
    current_time = day_start
    
    for event in events_on_date:
        event_start = max(event['start_time'], day_start)
        event_end = min(event['end_time'], day_end)
        
        # If there's a gap before this event
        if current_time < event_start:
            available_slots.append((current_time, event_start))
        
        # Move current_time to the end of this event
        current_time = max(current_time, event_end)
    
    # Check if there's time remaining at the end of the day
    if current_time < day_end:
        available_slots.append((current_time, day_end))
    
    return available_slots