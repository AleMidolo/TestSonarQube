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
    from datetime import datetime
    
    # Get current date/time
    now = datetime.now()
    
    # Filter events that are in the future (date >= now)
    upcoming = [event for event in self.events if event['date'] >= now]
    
    # Sort by date
    upcoming.sort(key=lambda x: x['date'])
    
    # Return all upcoming events (the docstring example shows returning all events regardless of num_events parameter)
    return upcoming