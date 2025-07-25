def dehydrate_timedelta(value):
    """
    使用 `timedelta` 的值来生成 `Structure` 类。
    用于 `time` 值的转换器。

    :param value: 
    :type value: timedelta
    :return: 
    """
    if not value:
        return None
        
    days = value.days
    seconds = value.seconds
    microseconds = value.microseconds
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'microseconds': microseconds
    }