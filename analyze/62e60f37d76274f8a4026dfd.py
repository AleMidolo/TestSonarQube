from datetime import time

def dehydrate_time(value):
    """
    Deshidratador para valores de tipo `time`.

    :param value: Valor de tipo `time` a deshidratar.
    :type value: time
    :return: Representación en cadena del tiempo en formato HH:MM:SS.
    :rtype: str
    """
    if not isinstance(value, time):
        raise TypeError("El valor debe ser de tipo `time`.")
    
    return value.strftime("%H:%M:%S")