from datetime import time

def dehydrate_time(value):
    """
    Dehydrator for `time` values.

    :param value: The time value to dehydrate.
    :type value: time
    :return: A string representation of the time in ISO format.
    :rtype: str
    """
    if not isinstance(value, time):
        raise TypeError("Expected a time object")
    return value.isoformat()