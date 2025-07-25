def format_dt(dt):
    """
    Format a datetime in the way that D* nodes expect.
    """
    return dt.strftime('%Y-%m-%dT%H:%M:%S') if dt else None