def dehydrate_timedelta(value):
    """
    `timedelta` मानों के लिए डिहाइड्रेटर।  

    :param value:  
    :type value: timedelta  
    :return:  
    """
    if value is None:
        return None
        
    # Convert timedelta to total seconds
    total_seconds = int(value.total_seconds())
    
    # Convert to hours, minutes, seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    # Format as string HH:MM:SS
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"