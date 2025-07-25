def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: The Point object to dehydrate.
    :type value: Point
    :return: A dictionary representation of the Point object.
    :rtype: dict
    """
    if not isinstance(value, Point):
        raise TypeError("Expected a Point object")
    
    return {
        'x': value.x,
        'y': value.y,
        'z': value.z if hasattr(value, 'z') else None
    }