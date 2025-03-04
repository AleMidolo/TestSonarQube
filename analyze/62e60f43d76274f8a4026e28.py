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
    if tz is not None:
        # If timezone provided, create timezone object
        if isinstance(tz, str):
            offset = int(tz.replace('UTC', ''))
            tz = timezone(timedelta(hours=offset))
        return time(hour=int(hours), 
                   minute=int(minutes),
                   second=int(seconds),
                   microsecond=int(microseconds),
                   tzinfo=tz)
    else:
        return time(hour=int(hours),
                   minute=int(minutes), 
                   second=int(seconds),
                   microsecond=int(microseconds))