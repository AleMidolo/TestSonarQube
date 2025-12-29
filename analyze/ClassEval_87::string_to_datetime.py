def string_to_datetime(self, string):
    """
        Convert the time string into a datetime instance
        :param string: string, string before format conversion
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')