def get_events(self, date):
    """
        获取给定日期的所有事件。
        :param date: 要获取事件的日期，datetime。
        :return: 给定日期的事件列表，list。
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': '新年'}]
        >>> calendar.get_events(datetime(2023, 1, 1, 0, 0))
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': '新年'}]
        """
    events_on_date = []
    target_date = date.date() if isinstance(date, datetime) else date
    for event in self.events:
        event_date = event['date']
        if isinstance(event_date, datetime):
            event_date = event_date.date()
        if event_date == target_date:
            events_on_date.append(event)
    return events_on_date