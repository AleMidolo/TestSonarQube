def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds: Nanoseconds since midnight
    :param tz: Optional timezone 
    :return: Time
    """
    from datetime import time, timezone, timedelta
    
    # Calculate hours, minutes, seconds and microseconds from nanoseconds
    total_seconds = nanoseconds // 1_000_000_000
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    microseconds = int((nanoseconds % 1_000_000_000) // 1000)

    # If timezone is provided, create timezone object
    if tz is not None:
        if isinstance(tz, str):
            offset = int(tz)
            tz = timezone(timedelta(hours=offset))
    
    # Create and return time object
    return time(
        hour=hours,
        minute=minutes,
        second=seconds,
        microsecond=microseconds,
        tzinfo=tz
    )