def add_event(self, event):
    """
        Agrega un evento al calendario.
        :param event: El evento que se va a agregar al calendario, dict.
        >>> calendar = CalendarUtil()
        >>> calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Año Nuevo'})
        >>> calendar.events
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'Año Nuevo'}]
        """
    self.events.append(event)