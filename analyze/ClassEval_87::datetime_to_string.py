def datetime_to_string(self, datetime):
    """
        Convert a datetime instance to a string
        :param datetime: the datetime instance to convert
        :return: string, converted time string
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
    format = '%Y-%m-%d %H:%M:%S'
    return datetime.strftime(format)