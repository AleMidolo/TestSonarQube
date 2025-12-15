def get_available_slots(self, date):
        """
        Ottieni tutti gli slot di tempo disponibili in una data specifica.
        :param date: La data per cui ottenere gli slot di tempo disponibili, datetime.
        :return: Un elenco di slot di tempo disponibili nella data specificata, list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'Capodanno'}]
        >>> calendar.get_available_slots(datetime(2023, 1, 1))
        [(datetime.datetime(2023, 1, 1, 23, 0), datetime.datetime(2023, 1, 2, 0, 0))]
        """
        slots = []
        start_of_day = datetime(date.year, date.month, date.day, 0, 0)
        end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)

        last_end_time = start_of_day

        for event in self.events:
            if event['date'].date() == date.date():
                if last_end_time < event['start_time']:
                    slots.append((last_end_time, event['start_time']))
                last_end_time = max(last_end_time, event['end_time'])

        if last_end_time < end_of_day:
            slots.append((last_end_time, end_of_day))

        return slots