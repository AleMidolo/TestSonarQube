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
    
    return {
        'days': value.days,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }