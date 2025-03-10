from datetime import time

def dehydrate_time(value):
    """
    Disidratatore per valori di tipo `time`.

    :param value: Un oggetto di tipo `time`.
    :type value: time
    :return: Una stringa rappresentante il tempo nel formato "HH:MM:SS".
    :rtype: str
    """
    if not isinstance(value, time):
        raise TypeError("Il valore deve essere di tipo `time`.")
    
    return value.strftime("%H:%M:%S")