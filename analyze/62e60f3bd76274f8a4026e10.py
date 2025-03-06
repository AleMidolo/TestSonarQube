from datetime import timedelta

def dehydrate_timedelta(value):
    """
    Deshidratador para valores de `timedelta`.

    :param value: Un objeto `timedelta` que se desea deshidratar.
    :type value: timedelta
    :return: Un diccionario con las claves 'days', 'seconds', y 'microseconds'.
    :rtype: dict
    """
    if not isinstance(value, timedelta):
        raise TypeError("El valor debe ser un objeto timedelta.")
    
    return {
        'days': value.days,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }