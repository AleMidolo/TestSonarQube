def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: The Point object to dehydrate.
    :type value: Point
    :return: A dictionary representation of the Point object.
    :rtype: dict
    """
    if not hasattr(value, 'x') or not hasattr(value, 'y'):
        raise ValueError("The provided value does not have 'x' and 'y' attributes.")
    
    return {
        'x': value.x,
        'y': value.y
    }