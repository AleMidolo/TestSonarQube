def remove_event(self, event):
    """
        Rimuovi un evento dal calendario.
        :param event: L'evento da rimuovere dal calendario, dict.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Capodanno'}]
        >>> calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Capodanno'})
        >>> calendar.events
        []
        """
    self.events = [e for e in self.events if e != event]