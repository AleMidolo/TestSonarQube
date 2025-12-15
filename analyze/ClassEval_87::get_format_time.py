def get_format_time(self, year, month, day, hour, minute, second):
    """
    समय को प्रारूपित करें
    :param year: int
    :param month: int
    :param day: int
    :param hour: int
    :param minute: int
    :param second: int
    :return: प्रारूपित समय स्ट्रिंग
    >>> timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
    "2001-07-18 01:01:01"
    """
    
    dt = datetime.datetime(year, month, day, hour, minute, second)
    return dt.strftime("%Y-%m-%d %H:%M:%S")