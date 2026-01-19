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
    events_on_date = self.get_events(date)
    sorted_events = sorted(events_on_date, key=lambda x: x['start_time'])
    day_start = datetime.combine(date.date(), datetime.min.time())
    day_end = day_start + timedelta(days=1)
    available_slots = []
    current_time = day_start
    for event in sorted_events:
        event_start = event['start_time']
        event_end = event['end_time']
        if current_time < event_start:
            available_slots.append((current_time, event_start))
        current_time = max(current_time, event_end)
    if current_time < day_end:
        available_slots.append((current_time, day_end))
    return available_slots