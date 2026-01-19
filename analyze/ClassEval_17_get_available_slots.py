def get_available_slots(self, date):
    """
        获取给定日期的所有可用时间段。
        :param date: 要获取可用时间段的日期，datetime。
        :return: 给定日期的可用时间段列表，list。
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': '新年'}]
        >>> calendar.get_available_slots(datetime(2023, 1, 1))
        [(datetime.datetime(2023, 1, 1, 23, 0), datetime.datetime(2023, 1, 2, 0, 0))]
        """
    day_events = self.get_events(date)
    sorted_events = sorted(day_events, key=lambda x: x['start_time'])
    day_start = datetime.combine(date.date(), datetime.min.time())
    day_end = datetime.combine(date.date() + timedelta(days=1), datetime.min.time())
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