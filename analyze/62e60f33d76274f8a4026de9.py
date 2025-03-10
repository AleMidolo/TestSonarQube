def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: The Point object to dehydrate.
    :type value: Point
    :return: A tuple representing the dehydrated Point (x, y).
    :rtype: tuple
    """
    return (value.x, value.y)