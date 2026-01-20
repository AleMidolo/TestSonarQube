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
        event_start = event['start_time']
        event_end = event['end_time']
        
        # Verifica si el evento se solapa con el día dado
        if event_start < day_end and event_end > day_start:
            # Ajusta los tiempos del evento a los límites del día
            adjusted_start = max(event_start, day_start)
            adjusted_end = min(event_end, day_end)
            events_on_date.append((adjusted_start, adjusted_end))
    
    # Ordena los eventos por tiempo de inicio
    events_on_date.sort(key=lambda x: x[0])
    
    # Encuentra los intervalos disponibles
    available_slots = []
    current_time = day_start
    
    for event_start, event_end in events_on_date:
        # Si hay un hueco entre el tiempo actual y el inicio del evento
        if current_time < event_start:
            available_slots.append((current_time, event_start))
        # Actualiza el tiempo actual al final del evento
        current_time = max(current_time, event_end)
    
    # Agrega el último intervalo si hay tiempo disponible hasta el final del día
    if current_time < day_end:
        available_slots.append((current_time, day_end))
    
    return available_slots