def add_event(self, event):
    """
    将事件添加到日历中。
    :param event: 要添加到日历中的事件，字典。
    >>> calendar = CalendarUtil()
    >>> calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': '新年'})
    >>> calendar.events
    [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': '新年'}]

    """
    if not hasattr(self, 'events'):
        self.events = []
    self.events.append(event)