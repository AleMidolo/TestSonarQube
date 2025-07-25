def dehydrate_time(value):
    """
    `time` मानों के लिए डिहाइड्रेटर।  

    :param value: समय का मान
    :type value: datetime.time
    :return: समय को स्ट्रिंग के रूप में (HH:MM:SS)
    :rtype: str
    """
    return value.strftime("%H:%M:%S")