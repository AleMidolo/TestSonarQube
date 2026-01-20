def get_events(self, date):
    """
    Obtiene todos los eventos en una fecha dada.
    :param date: La fecha para obtener eventos, datetime.
    :return: Una lista de eventos en la fecha dada, list.
    >>> calendar = CalendarUtil()
    >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Año Nuevo'}]
    >>> calendar.get_events(datetime(2023, 1, 1, 0, 0))
    [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'Año Nuevo'}]

    """
    return [event for event in self.events if event['date'].date() == date.date()]