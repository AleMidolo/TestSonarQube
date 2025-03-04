def dehydrate_point(value):
    """
    Dehydrator for Point data.
    
    :param value: Point object to dehydrate
    :type value: Point 
    :return: Dictionary containing point coordinates
    """
    if value is None:
        return None
        
    return {
        'x': value.x,
        'y': value.y
    }