def dehydrate_point(value):
    """
    Deidratatore per i dati di tipo `Point`.

    :param value:  
    :type value: Point  
    :return: 
    """
    return {'x': value.x, 'y': value.y}