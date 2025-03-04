def hydrate_time(nanoseconds, tz=None):
    """
    Idratatore per valori di `Time` e `LocalTime`.

    :param nanoseconds:  
    :param tz:  
    :return: Time
    """
    from datetime import datetime, timezone, timedelta

    # Convert nanoseconds to seconds and microseconds
    seconds = nanoseconds // 1_000_000_000
    microseconds = (nanoseconds % 1_000_000_000) // 1000

    # Create base datetime at epoch
    dt = datetime.fromtimestamp(0, timezone.utc)
    
    # Add the time components
    dt = dt + timedelta(seconds=seconds, microseconds=microseconds)

    # Apply timezone if provided
    if tz is not None:
        if isinstance(tz, str):
            from zoneinfo import ZoneInfo
            dt = dt.astimezone(ZoneInfo(tz))
        else:
            dt = dt.astimezone(tz)

    return dt.time()