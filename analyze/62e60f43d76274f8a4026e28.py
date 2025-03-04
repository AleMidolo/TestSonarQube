def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds: Nanoseconds since midnight
    :param tz: Optional timezone 
    :return: Time
    """
    from datetime import datetime, time, timezone, timedelta

    # Convert nanoseconds to time components
    total_seconds = nanoseconds // 1_000_000_000
    remaining_nanos = nanoseconds % 1_000_000_000
    
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    microseconds = int(remaining_nanos // 1000)

    # Create time object
    if tz is None:
        return time(hours, minutes, seconds, microseconds)
    else:
        # Convert timezone string to timezone object if needed
        if isinstance(tz, str):
            offset = int(tz[:-2]) if len(tz) > 2 else int(tz)
            tz = timezone(timedelta(hours=offset))
            
        # Create datetime with timezone to handle the offset
        dt = datetime.now(tz).replace(
            hour=hours,
            minute=minutes, 
            second=seconds,
            microsecond=microseconds
        )
        return dt.timetz()