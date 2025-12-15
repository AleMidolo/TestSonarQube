def string_to_datetime(self, string):
    """
    将时间字符串转换为 datetime 实例
    :param string: 字符串, 转换格式之前的字符串
    :return: datetime 实例
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    datetime.datetime(2001, 7, 18, 1, 1, 1)
    """
    return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")