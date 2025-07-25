from datetime import datetime

def format_dt(dt):
    """
    Format a datetime in the way that D* nodes expect.
    """
    if not isinstance(dt, datetime):
        raise TypeError("Input must be a datetime object")
    
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")