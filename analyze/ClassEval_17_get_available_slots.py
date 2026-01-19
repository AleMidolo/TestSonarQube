def get_available_slots(self, date):
    """
    दिए गए दिनांक पर सभी उपलब्ध समय स्लॉट प्राप्त करें।
    :param date: उपलब्ध समय स्लॉट प्राप्त करने के लिए दिनांक,datetime.
    :return: दिए गए दिनांक पर उपलब्ध समय स्लॉट की एक सूची,list.
    >>> calendar = CalendarUtil()
    >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'नया साल'}]
    >>> calendar.get_available_slots(datetime(2023, 1, 1))
    [(datetime.datetime(2023, 1, 1, 23, 0), datetime.datetime(2023, 1, 2, 0, 0))]

    """
    from datetime import datetime, timedelta
    
    # Get the start and end of the given date
    day_start = date.replace(hour=0, minute=0, second=0, microsecond=0)
    day_end = day_start + timedelta(days=1)
    
    # Filter events for the given date
    day_events = []
    for event in self.events:
        event_date = event['date'].replace(hour=0, minute=0, second=0, microsecond=0)
        if event_date == day_start:
            day_events.append(event)
    
    # Sort events by start time
    day_events.sort(key=lambda x: x['start_time'])
    
    # Find available slots
    available_slots = []
    current_time = day_start
    
    for event in day_events:
        # If there's a gap between current_time and event start, add it as available slot
        if current_time < event['start_time']:
            available_slots.append((current_time, event['start_time']))
        # Move current_time to the end of this event
        current_time = max(current_time, event['end_time'])
    
    # If there's time left after the last event until end of day
    if current_time < day_end:
        available_slots.append((current_time, day_end))
    
    return available_slots