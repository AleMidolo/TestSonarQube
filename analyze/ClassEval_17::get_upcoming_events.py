def get_upcoming_events(self, num_events):
        """
        获取从给定日期开始的下一个 n 个即将发生的事件。
        :param date: 获取即将发生事件的起始日期，datetime。
        :param n: 要获取的即将发生事件的数量，int。
        :return: 从给定日期开始的n 个即将发生事件的列表，list。
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': '新年'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': '新年 2'}]
        >>> calendar.get_upcoming_events(1)
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 23, 0), 'description': '新年'}, {'date': datetime.datetime(2023, 1, 2, 0, 0), 'end_time': datetime.datetime(2023, 1, 2, 1, 0), 'description': '新年 2'}]

        """
        upcoming_events = []
        current_time = datetime.now()
        
        for event in self.events:
            if event['start_time'] >= current_time:
                upcoming_events.append(event)
        
        return upcoming_events[:num_events]