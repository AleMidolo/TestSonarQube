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
        formats = [
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y/%m/%d %H:%M:%S",
            "%Y-%m-%d",
            "%d/%m/%Y %H:%M:%S",
            "%d-%m-%Y %H:%M:%S"
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(string, fmt)
            except ValueError:
                continue
        
        # If standard formats don't work, try a more flexible approach
        # Split date and time parts
        parts = string.strip().split()
        
        if len(parts) >= 1:
            date_part = parts[0]
            time_part = parts[1] if len(parts) > 1 else "0:0:0"
            
            # Parse date
            date_components = date_part.replace('/', '-').split('-')
            year = int(date_components[0])
            month = int(date_components[1])
            day = int(date_components[2])
            
            # Parse time
            time_components = time_part.split(':')
            hour = int(time_components[0]) if len(time_components) > 0 else 0
            minute = int(time_components[1]) if len(time_components) > 1 else 0
            second = int(time_components[2]) if len(time_components) > 2 else 0
            
            return datetime(year, month, day, hour, minute, second)
    
    except Exception as e:
        raise ValueError(f"Unable to parse datetime string: {string}")