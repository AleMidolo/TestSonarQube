def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: The Point object to dehydrate.
    :type value: Point
    :return: A dictionary representation of the Point object.
    :rtype: dict
    """
    if not value:
        return None
    return {
        'x': value.x,
        'y': value.y,
        'z': value.z if hasattr(value, 'z') else None
    }