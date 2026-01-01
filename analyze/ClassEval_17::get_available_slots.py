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
    slots = []
    start_of_day = datetime.combine(date.date(), datetime.min.time())
    end_of_day = datetime.combine(date.date(), datetime.max.time())
    last_end_time = start_of_day
    for event in self.events:
        if event['date'].date() == date.date():
            if last_end_time < event['start_time']:
                slots.append((last_end_time, event['start_time']))
            last_end_time = max(last_end_time, event['end_time'])
    if last_end_time < end_of_day:
        slots.append((last_end_time, end_of_day))
    return slots