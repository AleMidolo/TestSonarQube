def dehydrate_point(value):
    """
    Deidratatore per i dati di tipo `Point`.

    :param value: Un oggetto di tipo `Point`.
    :type value: Point
    :return: Un dizionario con le coordinate x e y del punto.
    :rtype: dict
    """
    return {'x': value.x, 'y': value.y}