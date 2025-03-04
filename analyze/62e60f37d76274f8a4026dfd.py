def dehydrate_time(value):
    """
    Dehydrator for `time` values.

    :param value:
    :type value: Time 
    :return:
    """
    if not value:
        return None
        
    return value.strftime('%H:%M:%S')