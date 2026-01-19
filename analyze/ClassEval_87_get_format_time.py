def get_format_time(self, year, month, day, hour, minute, second):
    """
    获取格式化时间
    :param year: int
    :param month: int
    :param day: int
    :param hour: int
    :param minute: int
    :param second: int
    :return: 格式化的时间字符串
    >>> timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
    "2001-07-18 01:01:01"
    """
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"