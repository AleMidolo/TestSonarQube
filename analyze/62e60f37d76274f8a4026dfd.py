def dehydrate_time(value):
    """
    Dehydrator for `time` values.

    :param value: A time object to be dehydrated.
    :type value: Time
    :return: A string representation of the time in 'HH:MM:SS' format.
    """
    if value is None:
        return None
    return value.strftime('%H:%M:%S')