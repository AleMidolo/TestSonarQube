def remove_event(self, event):
        """
        कैलेंडर से एक इवेंट हटाएं।
        :param event: कैलेंडर से हटाने के लिए इवेंट, dict।
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'नया साल'}]
        >>> calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'नया साल'})
        >>> calendar.events
        []
        """
        self.events = [e for e in self.events if e != event]