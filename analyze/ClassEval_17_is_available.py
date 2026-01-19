def is_available(self, start_time, end_time):
    """
        检查日历在给定时间段内是否可用。
        :param start_time: 时间段的开始时间，datetime。
        :param end_time: 时间段的结束时间，datetime。
        :return: 如果日历在给定时间段内可用，则返回 True；否则返回 False，bool。
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': '新年'}]
        >>> calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0))
        False
        """
    for event in self.events:
        event_start = event['start_time']
        event_end = event['end_time']
        if not (end_time <= event_start or start_time >= event_end):
            return False
    return True