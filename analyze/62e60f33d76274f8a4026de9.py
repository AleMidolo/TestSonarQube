def dehydrate_point(value):
    """
    Dehydrator for Point data.
    
    :param value:
    :type value: Point 
    :return:
    """
    if value is None:
        return None
        
    return {
        'x': value.x,
        'y': value.y
    }