from datetime import timedelta

def dehydrate_timedelta(value):
    """
    Dehydrator for `timedelta` values.

    :param value: timedelta
    :type value: timedelta
    :return: A dictionary representation of the timedelta
    """
    if not isinstance(value, timedelta):
        raise ValueError("Expected a timedelta object")
    
    return {
        'days': value.days,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }