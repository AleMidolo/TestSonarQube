def remove_event(self, event):
    """
    Eliminar un evento del calendario.
    :param event: El evento que se va a eliminar del calendario, dict.
    >>> calendar = CalendarUtil()
    >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Año Nuevo'}]
    >>> calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Año Nuevo'})
    >>> calendar.events
    []

    """
    if event in self.events:
        self.events.remove(event)