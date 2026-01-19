from datetime import datetime, timedelta

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
    # Get the start and end of the given date
    day_start = datetime(date.year, date.month, date.day, 0, 0)
    day_end = datetime(date.year, date.month, date.day, 23, 59, 59)
    next_day_start = day_start + timedelta(days=1)
    
    # Filter events for the given date
    events_on_date = []
    for event in self.events:
        event_date = event['date']
        if event_date.year == date.year and event_date.month == date.month and event_date.day == date.day:
            events_on_date.append(event)
    
    # Sort events by start_time
    events_on_date.sort(key=lambda x: x['start_time'])
    
    # Find available slots
    available_slots = []
    
    if not events_on_date:
        # If no events, entire day is available
        available_slots.append((day_start, next_day_start))
    else:
        # Check for slot before first event
        first_event = events_on_date[0]
        if first_event['start_time'] > day_start:
            available_slots.append((day_start, first_event['start_time']))
        
        # Check for slots between events
        for i in range(len(events_on_date) - 1):
            current_event_end = events_on_date[i]['end_time']
            next_event_start = events_on_date[i + 1]['start_time']
            if current_event_end < next_event_start:
                available_slots.append((current_event_end, next_event_start))
        
        # Check for slot after last event
        last_event = events_on_date[-1]
        if last_event['end_time'] < next_day_start:
            available_slots.append((last_event['end_time'], next_day_start))
    
    return available_slots