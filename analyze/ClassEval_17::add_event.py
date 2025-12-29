def add_event(self, event):
    """
        कैलेंडर में एक घटना जोड़ें।
        :param event: कैलेंडर में जोड़ी जाने वाली घटना, dict।
        >>> calendar = CalendarUtil()
        >>> calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'नया साल'})
        >>> calendar.events
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'नया साल'}]
        """
    self.events.append(event)