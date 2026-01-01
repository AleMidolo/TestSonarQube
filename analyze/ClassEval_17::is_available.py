def is_available(self, start_time, end_time):
    """
        Verifica si hay disponibilidad en el calendario para un intervalo de tiempo dado.
        :param start_time: La hora de inicio del intervalo de tiempo, datetime.
        :param end_time: La hora de finalización del intervalo de tiempo, datetime.
        :return: True si el calendario está disponible para el intervalo de tiempo dado, False en caso contrario, bool.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Año Nuevo'}]
        >>> calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0))
        False
        """
    for event in self.events:
        event_start = event['start_time']
        event_end = event['end_time']
        if not (end_time <= event_start or start_time >= event_end):
            return False
    return True