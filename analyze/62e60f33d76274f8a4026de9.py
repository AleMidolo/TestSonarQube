def dehydrate_point(value):
    """
    पॉइंट डेटा के लिए डिहाइड्रेटर।

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