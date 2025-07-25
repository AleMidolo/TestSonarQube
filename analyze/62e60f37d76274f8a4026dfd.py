from datetime import time

def dehydrate_time(value):
    """
    `time` मानों के लिए डिहाइड्रेटर।  

    :param value:  
    :type value: Time  
    :return:  
    """
    if isinstance(value, time):
        return value.isoformat()
    else:
        raise TypeError("Expected a time object")