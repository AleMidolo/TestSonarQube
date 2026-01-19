def datetime_to_string(self, datetime):
    """
        将 datetime 实例转换为字符串
        :param datetime: 要转换的 datetime 实例
        :return: 字符串，转换后的时间字符串
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
    format = '%Y-%m-%d %H:%M:%S'
    return datetime.strftime(format)