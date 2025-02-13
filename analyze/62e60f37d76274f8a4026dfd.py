def dehydrate_time(value):
    """
    Dehydrator for `time` values.

    :param value: Time instance to dehydrate
    :type value: Time
    :return: Dictionary representation of the Time instance
    """
    if not isinstance(value, Time):
        raise ValueError("Expected a Time instance")
    
    return {
        'ticks': value.ticks,
        'hours': value.hours,
        'minutes': value.minutes,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }