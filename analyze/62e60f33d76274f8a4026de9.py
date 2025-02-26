def dehydrate_point(value):  
    """
    Deshidratador para datos de tipo `Point`.  

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