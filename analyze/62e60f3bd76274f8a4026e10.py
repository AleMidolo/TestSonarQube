from datetime import timedelta

def dehydrate_timedelta(value):
    """
    Deidratatore per valori di tipo `timedelta`.

    :param value:  
    :type value: timedelta  
    :return: 
    """
    if not isinstance(value, timedelta):
        raise ValueError("Il valore deve essere di tipo timedelta.")
    return value.total_seconds()