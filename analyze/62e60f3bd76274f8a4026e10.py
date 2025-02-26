from datetime import timedelta

def dehydrate_timedelta(value):
    """
    Deidratatore per valori di tipo `timedelta`.

    :param value: 
    :type value: timedelta  
    :return: 
    """
    if not isinstance(value, timedelta):
        raise ValueError("Input must be a timedelta object.")
    
    total_seconds = int(value.total_seconds())
    return total_seconds