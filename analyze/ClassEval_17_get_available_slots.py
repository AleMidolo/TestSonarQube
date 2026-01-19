def get_available_slots(self, date):
    """
    Obtiene todos los intervalos de tiempo disponibles en una fecha dada.
    :param date: La fecha para la que se obtienen los intervalos de tiempo disponibles, datetime.
    :return: Una lista de intervalos de tiempo disponibles en la fecha dada, list.
    >>> calendar = CalendarUtil()
    >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'Año Nuevo'}]
    >>> calendar.get_available_slots(datetime(2023, 1, 1))
    [(datetime.datetime(2023, 1, 1, 23, 0), datetime.datetime(2023, 1, 2, 0, 0))]

    """
    from datetime import datetime, timedelta
    
    # Define el inicio y fin del día
    day_start = datetime(date.year, date.month, date.day, 0, 0)
    day_end = datetime(date.year, date.month, date.day, 0, 0) + timedelta(days=1)
    
    # Filtra eventos que ocurren en la fecha dada
    events_on_date = []
    for event in self.events:
        event_date = event['date']
        if event_date.year == date.year and event_date.month == date.month and event_date.day == date.day:
            events_on_date.append(event)
    
    # Ordena eventos por hora de inicio
    events_on_date.sort(key=lambda x: x['start_time'])
    
    # Encuentra los intervalos disponibles
    available_slots = []
    current_time = day_start
    
    for event in events_on_date:
        event_start = event['start_time']
        event_end = event['end_time']
        
        # Si hay un hueco antes del evento
        if current_time < event_start:
            available_slots.append((current_time, event_start))
        
        # Actualiza el tiempo actual al final del evento
        if event_end > current_time:
            current_time = event_end
    
    # Si hay tiempo disponible después del último evento
    if current_time < day_end:
        available_slots.append((current_time, day_end))
    
    return available_slots