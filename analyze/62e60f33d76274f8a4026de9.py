def dehydrate_point(value):
    """
    पॉइंट डेटा के लिए डिहाइड्रेटर।

    :param value: The Point object to be dehydrated.
    :type value: Point
    :return: A dictionary representing the dehydrated Point data.
    :rtype: dict
    """
    if not isinstance(value, Point):
        raise TypeError("Expected a Point object")
    
    return {
        'x': value.x,
        'y': value.y
    }