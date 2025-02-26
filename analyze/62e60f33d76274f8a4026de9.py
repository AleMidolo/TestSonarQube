def dehydrate_point(value):
    """
    पॉइंट डेटा के लिए डिहाइड्रेटर।

    :param value: Point object to dehydrate
    :type value: Point  
    :return: A dictionary representation of the Point
    """
    if not isinstance(value, Point):
        raise ValueError("Expected a Point instance")
    
    return {
        'x': value.x,
        'y': value.y,
        'z': value.z if hasattr(value, 'z') else None
    }