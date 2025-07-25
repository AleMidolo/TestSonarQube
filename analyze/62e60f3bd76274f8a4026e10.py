from datetime import timedelta

def dehydrate_timedelta(value):
    """
    Dehydrator for `timedelta` values.

    :param value: The timedelta object to dehydrate.
    :type value: timedelta
    :return: A dictionary representation of the timedelta.
    :rtype: dict
    """
    if not isinstance(value, timedelta):
        raise TypeError("Expected a timedelta object.")
    
    return {
        'days': value.days,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }