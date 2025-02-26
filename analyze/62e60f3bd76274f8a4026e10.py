from datetime import timedelta

def dehydrate_timedelta(value):
    """
    `timedelta` मानों के लिए डिहाइड्रेटर।  

    :param value:  
    :type value: timedelta  
    :return:  
    """
    if not isinstance(value, timedelta):
        raise ValueError("Input must be a timedelta object.")
    
    total_seconds = int(value.total_seconds())
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }