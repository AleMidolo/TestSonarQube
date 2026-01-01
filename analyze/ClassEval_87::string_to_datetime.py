def string_to_datetime(self, string):
    """
        समय स्ट्रिंग को datetime उदाहरण में परिवर्तित करें
        :param string: स्ट्रिंग, प्रारूप परिवर्तित करने से पहले की स्ट्रिंग
        :return: datetime उदाहरण
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats_to_try = ['%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y/%m/%d %H:%M', '%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d/%m/%Y %H:%M:%S', '%d-%m-%Y', '%d/%m/%Y']
    for fmt in formats_to_try:
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
            parts = normalized_string.split()
            date_part = parts[0]
            time_part = parts[1] if len(parts) > 1 else '0:0:0'
            date_parts = date_part.replace('-', '/').split('/')
            year = int(date_parts[0])
            month = int(date_parts[1])
            day = int(date_parts[2])
            time_parts = time_part.replace(':', ' ').split()
            hour = int(time_parts[0]) if len(time_parts) > 0 else 0
            minute = int(time_parts[1]) if len(time_parts) > 1 else 0
            second = int(time_parts[2]) if len(time_parts) > 2 else 0
            return datetime.datetime(year, month, day, hour, minute, second)
        except:
            raise ValueError(f'Unable to parse time string: {string}')