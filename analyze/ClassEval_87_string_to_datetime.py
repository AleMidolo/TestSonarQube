def string_to_datetime(self, string):
    """
    Convierte la cadena de tiempo a una instancia de datetime
    :param string: string, cadena antes de convertir el formato
    :return: instancia de datetime
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    from datetime import datetime
    
    # Split date and time parts
    parts = string.split()
    date_part = parts[0]
    time_part = parts[1] if len(parts) > 1 else "0:0:0"
    
    # Parse date components
    year, month, day = map(int, date_part.split('-'))
    
    # Parse time components
    hour, minute, second = map(int, time_part.split(':'))
    
    # Create datetime object
    return datetime(year, month, day, hour, minute, second)