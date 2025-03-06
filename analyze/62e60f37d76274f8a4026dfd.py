def dehydrate_time(value):
    """
    Deshidratador para valores de tipo `time`.

    :param value: Valor de tipo `time` a deshidratar.
    :type value: datetime.time
    :return: Representación en cadena del tiempo en formato HH:MM:SS.
    :rtype: str
    """
    if value is None:
        return None
    return value.strftime('%H:%M:%S')