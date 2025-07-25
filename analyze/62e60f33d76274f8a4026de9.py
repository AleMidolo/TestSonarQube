def dehydrate_point(value):
    """
    Deshidratador para datos de tipo `Point`.

    :param value: Un objeto de tipo `Point`.
    :type value: Point
    :return: Una tupla con las coordenadas (x, y) del punto.
    :rtype: tuple
    """
    return (value.x, value.y)