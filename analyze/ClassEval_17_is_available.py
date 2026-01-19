def is_available(self, start_time, end_time):
    """
        दिए गए समय स्लॉट के लिए कैलेंडर उपलब्ध है या नहीं, यह जांचें।
        :param start_time: समय स्लॉट का प्रारंभ समय,datetime.
        :param end_time: समय स्लॉट का अंत समय,datetime.
        :return: यदि कैलेंडर दिए गए समय स्लॉट के लिए उपलब्ध है, तो True, अन्यथा False,bool.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'नया साल'}]
        >>> calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0))
        False
        """
    for event in self.events:
        event_start = event['start_time']
        event_end = event['end_time']
        if start_time < event_end and end_time > event_start:
            return False
    return True