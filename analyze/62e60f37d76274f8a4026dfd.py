def dehydrate_time(value):
    """
    Disidratatore per valori di tipo `time`.

    :param value: 
    :type value: Time
    :return: String representation of the time in 'HH:MM:SS' format.
    """
    if value is None:
        return None
    return value.strftime('%H:%M:%S')