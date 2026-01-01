def get_upcoming_events(self, num_events):
    """
        Obtiene los próximos n eventos futuros a partir de una fecha dada.
        :param date: La fecha a partir de la cual obtener eventos futuros, datetime.
        :param n: El número de eventos futuros a obtener, int.
        :return: Una lista de los próximos n eventos futuros a partir de la fecha dada, list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'Año Nuevo'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'Año Nuevo 2'}]
        >>> calendar.get_upcoming_events(1)
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 23, 0), 'description': 'Año Nuevo'}, {'date': datetime.datetime(2023, 1, 2, 0, 0), 'end_time': datetime.datetime(2023, 1, 2, 1, 0), 'description': 'Año Nuevo 2'}]
        """
    now = datetime.now()
    future_events = []
    for event in self.events:
        if 'start_time' in event and event['start_time'] >= now:
            future_events.append(event)
        elif 'date' in event and event['date'] >= now:
            future_events.append(event)
    future_events.sort(key=lambda x: x.get('start_time', x.get('date')))
    return future_events[:num_events]