def dehydrate_point(value):
    """
    Deidratatore per i dati di tipo `Point`.

    :param value: Un oggetto di tipo `Point`.
    :type value: Point
    :return: Una rappresentazione serializzata del punto, tipicamente una tupla (x, y).
    :rtype: tuple
    """
    return (value.x, value.y)