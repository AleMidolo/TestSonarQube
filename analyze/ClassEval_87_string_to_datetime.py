def string_to_datetime(self, string):
    """
    Converte la stringa di tempo in un'istanza di datetime
    :param string: stringa, stringa prima della conversione del formato
    :return: istanza di datetime
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    from datetime import datetime
    
    # Parse the string to datetime object
    dt = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    
    return dt