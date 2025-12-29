def string_to_datetime(self, string):
    """
        समय स्ट्रिंग को datetime उदाहरण में परिवर्तित करें
        :param string: स्ट्रिंग, प्रारूप परिवर्तित करने से पहले की स्ट्रिंग
        :return: datetime उदाहरण
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats_to_try = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y', '%Y.%m.%d %H:%M:%S', '%Y.%m.%d %H:%M', '%Y.%m.%d']
    for fmt in formats_to_try:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    try:
        from dateutil import parser
        return parser.parse(string)
    except ImportError:
        raise ValueError(f'Unable to parse date string: {string}')