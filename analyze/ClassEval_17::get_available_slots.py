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
    events_on_date = self.get_events(date)
    sorted_events = sorted(events_on_date, key=lambda x: x['start_time'])
    day_start = datetime.combine(date.date(), datetime.min.time())
    day_end = datetime.combine(date.date(), datetime.max.time())
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