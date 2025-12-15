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
        start_of_day = datetime(date.year, date.month, date.day, 0, 0)
        end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)
        available_slots = []
        last_end_time = start_of_day

        for event in self.events:
            if event['date'].date() == date.date():
                if last_end_time < event['start_time']:
                    available_slots.append((last_end_time, event['start_time']))
                last_end_time = max(last_end_time, event['end_time'])

        if last_end_time < end_of_day:
            available_slots.append((last_end_time, end_of_day))

        return available_slots