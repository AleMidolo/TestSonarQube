def get_upcoming_events(self, num_events):
        """
        दिए गए दिनांक से अगले n आगामी घटनाओं को प्राप्त करें।
        :param date: आगामी घटनाओं को प्राप्त करने के लिए दिनांक,datetime.
        :param n: प्राप्त करने के लिए आगामी घटनाओं की संख्या,int.
        :return: दिए गए दिनांक से अगले n आगामी घटनाओं की सूची,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'नया साल'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'नया साल 2'}]
        >>> calendar.get_upcoming_events(1)
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 23, 0), 'description': 'नया साल'}, {'date': datetime.datetime(2023, 1, 2, 0, 0), 'end_time': datetime.datetime(2023, 1, 2, 1, 0), 'description': 'नया साल 2'}]

        """
        upcoming_events = []
        current_date = datetime.now()

        for event in self.events:
            if event['date'] >= current_date:
                upcoming_events.append(event)
                if len(upcoming_events) == num_events:
                    break

        return upcoming_events