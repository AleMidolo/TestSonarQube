from datetime import time

def dehydrate_time(value):
    """
    `time` मानों के लिए डिहाइड्रेटर।  

    :param value: समय का मान
    :type value: time
    :return: समय को स्ट्रिंग के रूप में (HH:MM:SS)
    :rtype: str
    """
    if not isinstance(value, time):
        raise TypeError("Expected a time object")
    return value.strftime("%H:%M:%S")