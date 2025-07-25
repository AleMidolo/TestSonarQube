def dehydrate_timedelta(value):
    """
    Dehydrator for `timedelta` values.

    :param value:
    :type value: timedelta 
    :return:
    """
    if value is None:
        return None
        
    # Convert timedelta to total seconds
    total_seconds = int(value.total_seconds())
    
    # Return string representation in format "HH:MM:SS"
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"