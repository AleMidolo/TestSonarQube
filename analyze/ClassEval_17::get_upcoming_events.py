def get_upcoming_events(self, num_events):
    """
        Ottieni i prossimi n eventi in arrivo da una data specificata.
        :param date: La data da cui ottenere gli eventi in arrivo, datetime.
        :param n: Il numero di eventi in arrivo da ottenere, int.
        :return: Una lista dei prossimi n eventi in arrivo dalla data specificata, list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'Capodanno'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'Capodanno 2'}]
        >>> calendar.get_upcoming_events(1)
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 23, 0), 'description': 'Capodanno'}, {'date': datetime.datetime(2023, 1, 2, 0, 0), 'end_time': datetime.datetime(2023, 1, 2, 1, 0), 'description': 'Capodanno 2'}]

        """
    sorted_events = sorted(self.events, key=lambda x: x['start_time'])
    return sorted_events[:num_events]