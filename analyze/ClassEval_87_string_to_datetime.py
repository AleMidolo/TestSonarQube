def string_to_datetime(self, string):
    """
    Convierte la cadena de tiempo a una instancia de datetime
    :param string: string, cadena antes de convertir el formato
    :return: instancia de datetime
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    from datetime import datetime
    
    # Parse the string to datetime object
    # Handle various common datetime formats
    try:
        # Try parsing with datetime.strptime for common formats
        dt = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            # Try with single digit month/day/hour/minute/second
            parts = string.split()
            date_part = parts[0]
            time_part = parts[1] if len(parts) > 1 else "0:0:0"
            
            date_components = date_part.split('-')
            time_components = time_part.split(':')
            
            year = int(date_components[0])
            month = int(date_components[1])
            day = int(date_components[2])
            
            hour = int(time_components[0]) if len(time_components) > 0 else 0
            minute = int(time_components[1]) if len(time_components) > 1 else 0
            second = int(time_components[2]) if len(time_components) > 2 else 0
            
            dt = datetime(year, month, day, hour, minute, second)
        except (ValueError, IndexError):
            raise ValueError(f"Unable to parse datetime string: {string}")
    
    return dt