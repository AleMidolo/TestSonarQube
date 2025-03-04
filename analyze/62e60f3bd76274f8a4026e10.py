def dehydrate_timedelta(value):
    """
    Deidratatore per valori di tipo `timedelta`.

    :param value: Valore timedelta da deidratare
    :type value: timedelta
    :return: Stringa rappresentante il timedelta in formato ISO 8601
    """
    days = value.days
    seconds = value.seconds
    microseconds = value.microseconds
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    result = "P"
    
    if days:
        result += f"{days}D"
    
    if hours or minutes or seconds or microseconds:
        result += "T"
        if hours:
            result += f"{hours}H"
        if minutes:
            result += f"{minutes}M"
        if seconds:
            if microseconds:
                result += f"{seconds}.{microseconds:06d}S"
            else:
                result += f"{seconds}S"
        elif microseconds:
            result += f"0.{microseconds:06d}S"
            
    if result == "P":
        result = "PT0S"
        
    return result