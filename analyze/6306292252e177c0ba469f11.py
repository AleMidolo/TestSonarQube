from datetime import datetime

def format_dt(dt):
    """
    Format a datetime in the way that D* nodes expect.
    """
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    
    # Format the datetime as 'YYYY-MM-DD HH:MM:SS'
    return dt.strftime('%Y-%m-%d %H:%M:%S')