def string_to_datetime(self, string):
    """
    Convierte la cadena de tiempo a una instancia de datetime
    :param string: string, cadena antes de convertir el formato
    :return: instancia de datetime
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    from datetime import datetime
    
    # Try multiple formats to handle both padded and unpadded values
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%#m-%#d %H:%M:%S",  # Windows
        "%Y-%-m-%-d %H:%M:%S",  # Unix/Linux
    ]
    
    # Simple approach: normalize the string first
    parts = string.split()
    date_part = parts[0]
    time_part = parts[1] if len(parts) > 1 else "0:0:0"
    
    date_components = date_part.split('-')
    time_components = time_part.split(':')
    
    year = int(date_components[0])
    month = int(date_components[1])
    day = int(date_components[2])
    hour = int(time_components[0])
    minute = int(time_components[1])
    second = int(time_components[2])
    
    return datetime(year, month, day, hour, minute, second)