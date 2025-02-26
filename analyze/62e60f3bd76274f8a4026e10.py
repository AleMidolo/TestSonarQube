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
    return {
        'days': value.days,
        'seconds': total_seconds % 86400,
        'microseconds': value.microseconds
    }