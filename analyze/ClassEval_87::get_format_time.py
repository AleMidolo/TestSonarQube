def get_format_time(self, year, month, day, hour, minute, second):
    """
    ottieni tempo formattato
    :param year: int
    :param month: int
    :param day: int
    :param hour: int
    :param minute: int
    :param second: int
    :return: stringa di tempo formattata
    >>> timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
    "2001-07-18 01:01:01"
    """
    dt = datetime.datetime(year, month, day, hour, minute, second)
    return dt.strftime('%Y-%m-%d %H:%M:%S')