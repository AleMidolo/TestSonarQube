def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]
        >>> calendar.get_upcoming_events(1)
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}, {'date': datetime.datetime(2023, 1, 2, 0, 0), 'end_time': datetime.datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]

        """
        upcoming_events = []
        current_time = datetime.now()
        
        for event in self.events:
            if event['start_time'] > current_time:
                upcoming_events.append(event)
        
        return upcoming_events[:num_events]