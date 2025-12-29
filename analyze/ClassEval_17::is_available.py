def is_available(self, start_time, end_time):
    """
        Controlla se il calendario è disponibile per un determinato intervallo di tempo.
        :param start_time: L'orario di inizio dell'intervallo di tempo, datetime.
        :param end_time: L'orario di fine dell'intervallo di tempo, datetime.
        :return: True se il calendario è disponibile per l'intervallo di tempo dato, False altrimenti, bool.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Capodanno'}]
        >>> calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0))
        False
        """
    for event in self.events:
        if start_time < event['end_time'] and end_time > event['start_time']:
            return False
    return True