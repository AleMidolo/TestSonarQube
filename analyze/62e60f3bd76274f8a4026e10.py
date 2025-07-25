def dehydrate_timedelta(value):
    """
    Deidratatore per valori di tipo `timedelta`.

    :param value:  
    :type value: timedelta  
    :return: 
    """
    if value is None:
        return None
        
    total_seconds = int(value.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"