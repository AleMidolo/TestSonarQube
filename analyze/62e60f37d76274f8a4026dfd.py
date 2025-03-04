def dehydrate_time(value):
    """
    Deshidratador para valores de tipo `time`.

    :param value:  
    :type value: Time  
    :return:  
    """
    if value is None:
        return None
        
    return value.strftime('%H:%M:%S')