def dehydrate_point(value):
    """
    पॉइंट डेटा के लिए डिहाइड्रेटर।

    :param value: पॉइंट ऑब्जेक्ट
    :type value: Point
    :return: पॉइंट के निर्देशांक (x, y) का टपल
    :rtype: tuple
    """
    if hasattr(value, 'x') and hasattr(value, 'y'):
        return (value.x, value.y)
    else:
        raise ValueError("Invalid Point object provided. Expected attributes 'x' and 'y'.")