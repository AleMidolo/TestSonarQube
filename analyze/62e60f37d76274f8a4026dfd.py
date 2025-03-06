from datetime import time

def dehydrate_time(value):
    """
    Disidratatore per valori di tipo `time`.

    :param value: 
    :type value: Time
    :return: String representation of the time in 'HH:MM:SS' format.
    :rtype: str
    """
    if not isinstance(value, time):
        raise TypeError("Expected a time object")
    
    return value.strftime('%H:%M:%S')