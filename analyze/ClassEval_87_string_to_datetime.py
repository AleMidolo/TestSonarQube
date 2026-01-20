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
    dt = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    
    return dt