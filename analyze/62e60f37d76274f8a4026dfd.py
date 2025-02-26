def dehydrate_time(value):
    """
    Deshidratador para valores de tipo `time`.

    :param value: A time object to be dehydrated.
    :type value: time  
    :return: A string representation of the time in 'HH:MM:SS' format.
    """
    if value is None:
        return None
    return value.strftime('%H:%M:%S')