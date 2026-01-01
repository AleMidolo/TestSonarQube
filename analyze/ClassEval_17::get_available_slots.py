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
    slots = []
    start_of_day = datetime.combine(date.date(), datetime.min.time())
    end_of_day = datetime.combine(date.date(), datetime.max.time())
    last_end_time = start_of_day
    for event in sorted(self.events, key=lambda x: x['start_time']):
        if event['start_time'] > last_end_time:
            slots.append((last_end_time, event['start_time']))
        last_end_time = max(last_end_time, event['end_time'])
    if last_end_time < end_of_day:
        slots.append((last_end_time, end_of_day))
    return slots