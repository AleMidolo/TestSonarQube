from datetime import timedelta

def dehydrate_timedelta(value):
    """
    Dehydrator for `timedelta` values.

    :param value: A timedelta object to be dehydrated.
    :type value: timedelta
    :return: A dictionary representation of the timedelta.
    """
    if not isinstance(value, timedelta):
        raise ValueError("The value must be a timedelta object.")
    
    total_seconds = int(value.total_seconds())
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }