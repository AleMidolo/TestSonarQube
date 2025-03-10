from datetime import datetime

def format_dt(dt):
    """
    Format a datetime in the way that D* nodes expect.
    
    Args:
        dt (datetime): The datetime object to format.
    
    Returns:
        str: The formatted datetime string.
    """
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object.")
    
    # Format the datetime in the expected way for D* nodes
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")