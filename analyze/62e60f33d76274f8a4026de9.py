def dehydrate_point(value):
    """
    Deidratatore per i dati di tipo `Point`.

    :param value:  
    :type value: Point  
    :return: 
    """
    if not isinstance(value, Point):
        raise ValueError("Expected a Point instance")
    
    return {
        'x': value.x,
        'y': value.y
    }