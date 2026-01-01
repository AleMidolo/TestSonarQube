def get_events(self, date):
    """
        दिए गए तारीख पर सभी घटनाएँ प्राप्त करें।
        :param date: घटनाएँ प्राप्त करने के लिए तारीख,datetime.
        :return: दिए गए तारीख पर घटनाओं की एक सूची,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'नया साल'}]
        >>> calendar.get_events(datetime(2023, 1, 1, 0, 0))
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'नया साल'}]

        """
    events_on_date = []
    for event in self.events:
        if event['date'].date() == date.date():
            events_on_date.append(event)
    return events_on_date