from datetime import timedelta

def dehydrate_timedelta(value):
    """
    Deshidratador para valores de `timedelta`.

    :param value: 
    :type value: timedelta  
    :return: 
    """
    if not isinstance(value, timedelta):
        raise ValueError("El valor debe ser una instancia de timedelta.")
    
    total_seconds = int(value.total_seconds())
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }