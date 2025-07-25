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
    base_dt = datetime(1970, 1, 1)

    # Add the time delta
    dt = base_dt + timedelta(seconds=seconds, microseconds=microseconds)

    # Handle timezone if provided
    if tz is not None:
        if isinstance(tz, str):
            from datetime import tzinfo
            import pytz
            tz = pytz.timezone(tz)
        elif isinstance(tz, int):
            tz = timezone(timedelta(hours=tz))
        dt = dt.replace(tzinfo=tz)

    return dt.time()