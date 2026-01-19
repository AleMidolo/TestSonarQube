def string_to_datetime(self, string):
    """
    Convert the time string to a datetime instance
    :param string: string, string before converting format
    :return: datetime instance
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    from datetime import datetime
    
    # Parse the string to datetime
    # Handle various common datetime formats
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S.%f",
    ]
    
    # Try parsing with standard formats first
    for fmt in formats:
        try:
            return datetime.strptime(string, fmt)
        except ValueError:
            continue
    
    # If standard formats fail, try a more flexible approach
    # Split date and time parts
    parts = string.split()
    if len(parts) == 2:
        date_part, time_part = parts
        
        # Parse date
        date_components = date_part.replace('/', '-').split('-')
        year = int(date_components[0])
        month = int(date_components[1])
        day = int(date_components[2])
        
        # Parse time
        time_components = time_part.split(':')
        hour = int(time_components[0])
        minute = int(time_components[1])
        second = int(time_components[2]) if len(time_components) > 2 else 0
        
        return datetime(year, month, day, hour, minute, second)
    
    # Fallback: try to parse as date only
    return datetime.strptime(string, "%Y-%m-%d")