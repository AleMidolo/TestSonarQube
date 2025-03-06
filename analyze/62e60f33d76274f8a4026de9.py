def dehydrate_point(value):
    """
    पॉइंट डेटा के लिए डिहाइड्रेटर।

    :param value: पॉइंट ऑब्जेक्ट
    :type value: Point  
    :return: पॉइंट ऑब्जेक्ट के निर्देशांक (x, y) का टपल
    :rtype: tuple
    """
    return (value.x, value.y)