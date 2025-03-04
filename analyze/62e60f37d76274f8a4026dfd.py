def dehydrate_time(value):
    """
    Disidratatore per valori di tipo `time`.

    :param value: 
    :type value: Time
    :return:
    """
    if value is None:
        return None
    return value.isoformat()