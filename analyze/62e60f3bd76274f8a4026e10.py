from datetime import timedelta

def dehydrate_timedelta(value):
    """
    `timedelta` मानों के लिए डिहाइड्रेटर।  

    :param value:  
    :type value: timedelta  
    :return:  
    """
    if not isinstance(value, timedelta):
        raise TypeError("Expected a timedelta object")
    
    # Convert timedelta to total seconds and return as a float
    return value.total_seconds()