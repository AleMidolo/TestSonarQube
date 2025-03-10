def dehydrate_point(value):
    """
    Deidratatore per i dati di tipo `Point`.

    :param value: Un oggetto di tipo `Point`.
    :type value: Point
    :return: Una rappresentazione serializzata del punto.
    :rtype: dict
    """
    if not hasattr(value, 'x') or not hasattr(value, 'y'):
        raise ValueError("L'oggetto fornito non è un punto valido.")
    
    return {
        'x': value.x,
        'y': value.y
    }