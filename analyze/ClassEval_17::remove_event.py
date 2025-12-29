def remove_event(self, event):
    """
        从日历中移除一个事件。
        :param event: 要从日历中移除的事件，字典。
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': '新年'}]
        >>> calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': '新年'})
        >>> calendar.events
        []

        """
    if event in self.events:
        self.events.remove(event)