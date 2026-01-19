def string_to_datetime(self, string):
    """
    Convert the time string to a datetime instance
    :param string: string, string before converting format
    :return: datetime instance
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    from datetime import datetime
    
    # Try common datetime formats
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S.%f",
        "%Y-%m-%d",
        "%Y/%m/%d",
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(string, fmt)
        except ValueError:
            continue
    
    # If no format matches, raise an error
    raise ValueError(f"Unable to parse datetime string: {string}")