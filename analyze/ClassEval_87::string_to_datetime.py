def string_to_datetime(self, string):
    """
        समय स्ट्रिंग को datetime उदाहरण में परिवर्तित करें
        :param string: स्ट्रिंग, प्रारूप परिवर्तित करने से पहले की स्ट्रिंग
        :return: datetime उदाहरण
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y', '%Y.%m.%d %H:%M:%S', '%Y.%m.%d %H:%M', '%Y.%m.%d', '%d.%m.%Y %H:%M:%S', '%d.%m.%Y %H:%M', '%d.%m.%Y']
    for fmt in formats:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    string = string.strip()
    try:
        if ' ' in string:
            date_part, time_part = string.split(' ', 1)
        else:
            date_part = string
            time_part = None
        date_parts = date_part.replace('-', ' ').replace('/', ' ').replace('.', ' ').split()
        year = int(date_parts[0])
        month = int(date_parts[1]) if len(date_parts) > 1 else 1
        day = int(date_parts[2]) if len(date_parts) > 2 else 1
        hour = minute = second = 0
        if time_part:
            time_parts = time_part.replace(':', ' ').split()
            hour = int(time_parts[0]) if len(time_parts) > 0 else 0
            minute = int(time_parts[1]) if len(time_parts) > 1 else 0
            second = int(time_parts[2]) if len(time_parts) > 2 else 0
        return datetime.datetime(year, month, day, hour, minute, second)
    except (ValueError, IndexError):
        raise ValueError(f'Unable to parse time string: {string}')