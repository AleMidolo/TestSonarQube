def dehydrate_point(value):
    """
    Deshidratador para datos de tipo `Point`.

    :param value: 
    :type value: Point
    :return: Diccionario con las coordenadas x e y del punto.
    :rtype: dict
    """
    return {'x': value.x, 'y': value.y}