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
    result = []
    for event in self.events:
        if event['date'].date() == date.date():
            result.append(event)
    return result