def string_to_datetime(self, string):
    """
        समय स्ट्रिंग को datetime उदाहरण में परिवर्तित करें
        :param string: स्ट्रिंग, प्रारूप परिवर्तित करने से पहले की स्ट्रिंग
        :return: datetime उदाहरण
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y']
    for fmt in formats:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    normalized_string = string.strip()
    try:
        from dateutil import parser
        return parser.parse(normalized_string)
    except ImportError:
        try:
            return datetime.datetime.fromisoformat(normalized_string)
        except ValueError:
            parts = normalized_string.replace('-', ' ').replace('/', ' ').replace(':', ' ').split()
            if len(parts) >= 3:
                year = int(parts[0]) if len(parts[0]) == 4 else int(parts[2])
                month = int(parts[1])
                day = int(parts[2]) if len(parts[0]) == 4 else int(parts[0])
                hour = int(parts[3]) if len(parts) > 3 else 0
                minute = int(parts[4]) if len(parts) > 4 else 0
                second = int(parts[5]) if len(parts) > 5 else 0
                return datetime.datetime(year, month, day, hour, minute, second)
    raise ValueError(f'Unable to parse time string: {string}')