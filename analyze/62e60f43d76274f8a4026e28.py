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
    dt = datetime.fromtimestamp(seconds, tz or timezone.utc)
    
    # Add microseconds
    dt = dt.replace(microsecond=microseconds)

    # If no timezone specified, return naive time
    if tz is None:
        dt = dt.replace(tzinfo=None)

    return dt.time()