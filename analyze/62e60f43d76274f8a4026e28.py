def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds: Number of nanoseconds since midnight
    :param tz: Optional timezone 
    :return: Time
    """
    from datetime import time, timezone, timedelta
    
    # Calculate hours, minutes, seconds and microseconds from nanoseconds
    total_microseconds = nanoseconds // 1000
    hours = total_microseconds // (3600 * 1000000)
    remaining = total_microseconds % (3600 * 1000000)
    minutes = remaining // (60 * 1000000)
    remaining = remaining % (60 * 1000000)
    seconds = remaining // 1000000
    microseconds = remaining % 1000000

    # Create time object
    if tz is None:
        return time(hour=int(hours), 
                   minute=int(minutes),
                   second=int(seconds),
                   microsecond=int(microseconds))
    else:
        # If timezone provided, create time with timezone
        if isinstance(tz, str):
            # Convert string timezone offset to timedelta
            hours_offset = int(tz[1:3])
            minutes_offset = int(tz[3:]) if len(tz) > 3 else 0
            delta = timedelta(hours=hours_offset, minutes=minutes_offset)
            tz = timezone(delta if tz[0] == '+' else -delta)
            
        return time(hour=int(hours),
                   minute=int(minutes), 
                   second=int(seconds),
                   microsecond=int(microseconds),
                   tzinfo=tz)