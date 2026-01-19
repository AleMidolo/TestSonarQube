def get_available_slots(self, date):
    """
    Ottieni tutti gli slot di tempo disponibili in una data specifica.
    :param date: La data per cui ottenere gli slot di tempo disponibili, datetime.
    :return: Un elenco di slot di tempo disponibili nella data specificata, list.
    >>> calendar = CalendarUtil()
    >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'Capodanno'}]
    >>> calendar.get_available_slots(datetime(2023, 1, 1))
    [(datetime.datetime(2023, 1, 1, 23, 0), datetime.datetime(2023, 1, 2, 0, 0))]
    """
    from datetime import datetime, timedelta
    
    # Define the start and end of the day
    day_start = datetime(date.year, date.month, date.day, 0, 0)
    day_end = datetime(date.year, date.month, date.day, 23, 59, 59)
    # Adjust to next day midnight for proper slot calculation
    next_day_start = day_start + timedelta(days=1)
    
    # Filter events for the specified date
    events_on_date = []
    for event in self.events:
        event_date = event['date']
        if event_date.year == date.year and event_date.month == date.month and event_date.day == date.day:
            events_on_date.append(event)
    
    # Sort events by start time
    events_on_date.sort(key=lambda x: x['start_time'])
    
    # Find available slots
    available_slots = []
    current_time = day_start
    
    for event in events_on_date:
        event_start = event['start_time']
        event_end = event['end_time']
        
        # If there's a gap between current_time and event start, add it as available slot
        if current_time < event_start:
            available_slots.append((current_time, event_start))
        
        # Move current_time to the end of this event
        if event_end > current_time:
            current_time = event_end
    
    # Check if there's time remaining until end of day
    if current_time < next_day_start:
        available_slots.append((current_time, next_day_start))
    
    return available_slots