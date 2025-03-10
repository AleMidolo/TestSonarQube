def dehydrate_point(value):
    """
    Deshidratador para datos de tipo `Point`.

    :param value: Punto a deshidratar.
    :type value: Point
    :return: Diccionario con las coordenadas del punto.
    :rtype: dict
    """
    return {'x': value.x, 'y': value.y}