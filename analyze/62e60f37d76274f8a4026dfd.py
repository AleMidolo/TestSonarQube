def dehydrate_time(value):
    """
    Dehydrator for `time` values.

    :param value: The time value to dehydrate.
    :type value: datetime.time
    :return: A string representation of the time in 'HH:MM:SS' format.
    :rtype: str
    """
    if value is None:
        return None
    return value.strftime('%H:%M:%S')