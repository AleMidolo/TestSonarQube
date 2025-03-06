from datetime import datetime

def format_dt(dt):
    """
    Format a datetime in the way that D* nodes expect.
    
    Args:
        dt (datetime): The datetime object to format.
    
    Returns:
        str: The formatted datetime string.
    """
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')