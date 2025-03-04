def default_tzinfo(dt, tzinfo):
    if dt.tzinfo is not None:
        return dt
    return dt.replace(tzinfo=tzinfo)