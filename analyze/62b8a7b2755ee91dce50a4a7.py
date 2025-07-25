def default_tzinfo(dt, tzinfo):
    # If dt already has a tzinfo, return it unchanged
    if dt.tzinfo is not None:
        return dt
        
    # Otherwise, return a new datetime with the default tzinfo
    return dt.replace(tzinfo=tzinfo)