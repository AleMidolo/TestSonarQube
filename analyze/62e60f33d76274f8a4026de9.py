def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: A Point object to be dehydrated.
    :type value: Point
    :return: A dictionary representation of the Point object.
    """
    if not isinstance(value, Point):
        raise ValueError("Expected a Point instance")
    
    return {
        'x': value.x,
        'y': value.y,
        'z': value.z
    }