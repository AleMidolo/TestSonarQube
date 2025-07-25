from datetime import time

def dehydrate_time(value):
    """
    `time` मानों के लिए डिहाइड्रेटर।  

    :param value:  
    :type value: Time  
    :return:  
    """
    if not isinstance(value, time):
        raise TypeError("Expected a datetime.time object")
    
    return value.isoformat()