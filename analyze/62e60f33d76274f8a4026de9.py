def dehydrate_point(value):
    """
    Deshidratador para datos de tipo `Point`.

    :param value: Un objeto de tipo `Point`.
    :type value: Point
    :return: Una representación deshidratada del punto, típicamente una tupla (x, y).
    :rtype: tuple
    """
    return (value.x, value.y)