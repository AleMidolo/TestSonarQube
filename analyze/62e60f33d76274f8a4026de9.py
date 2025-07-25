def dehydrate_point(value):
    """
    Deidratatore per i dati di tipo `Point`.
    
    :param value: Point object to dehydrate
    :type value: Point
    :return: Dictionary containing x,y coordinates
    """
    if value is None:
        return None
        
    return {
        'x': value.x,
        'y': value.y
    }