def get_events(self, date):
    """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        >>> calendar.get_events(datetime(2023, 1, 1, 0, 0))
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]

        """
    return [event for event in self.events if event['date'].date() == date.date()]