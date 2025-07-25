def dehydrate_point(value):
    """
    पॉइंट डेटा के लिए डिहाइड्रेटर।

    :param value: Point object to be dehydrated.
    :type value: Point  
    :return: A dictionary representing the dehydrated point.
    :rtype: dict
    """
    if not hasattr(value, 'x') or not hasattr(value, 'y'):
        raise ValueError("The provided value does not have 'x' and 'y' attributes.")
    
    return {
        'x': value.x,
        'y': value.y
    }