def dehydrate_time(value):
    """
    `time` मानों के लिए डिहाइड्रेटर।  

    :param value:  
    :type value: Time  
    :return:  
    """
    if value is None:
        return None
    return value.strftime('%H:%M:%S')