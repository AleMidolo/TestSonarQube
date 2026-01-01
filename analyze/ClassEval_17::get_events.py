def get_events(self, date):
    """
        Ottieni tutti gli eventi in una data specifica.
        :param date: La data per cui ottenere gli eventi, datetime.
        :return: Una lista di eventi nella data specificata, list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'Capodanno'}]
        >>> calendar.get_events(datetime(2023, 1, 1, 0, 0))
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'Capodanno'}]
        """
    target_date = date.date() if isinstance(date, datetime) else date
    events_on_date = []
    for event in self.events:
        event_date = event['date'].date() if isinstance(event['date'], datetime) else event['date']
        if event_date == target_date:
            events_on_date.append(event)
    return events_on_date