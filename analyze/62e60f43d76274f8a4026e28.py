def hydrate_time(nanoseconds, tz=None):
    """
    Hydrator for `Time` and `LocalTime` values.

    :param nanoseconds:
    :param tz:
    :return: Time
    """
    from datetime import time, timezone, timedelta

    # Calculate hours, minutes, seconds and microseconds from nanoseconds
    total_seconds = nanoseconds // 1_000_000_000
    remaining_nanos = nanoseconds % 1_000_000_000
    
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    microseconds = int(remaining_nanos // 1000)

    # Handle timezone if provided
    if tz is not None:
        # Convert timezone offset to timedelta
        if isinstance(tz, int):
            tz = timezone(timedelta(seconds=tz))
        elif isinstance(tz, str):
            # Parse timezone string (assuming format like '+HH:MM' or '-HH:MM')
            sign = 1 if tz[0] == '+' else -1
            hours_offset = int(tz[1:3])
            minutes_offset = int(tz[4:6]) if len(tz) > 4 else 0
            tz = timezone(timedelta(hours=sign * hours_offset, 
                                  minutes=sign * minutes_offset))

    # Create and return time object
    return time(hour=hours % 24, 
               minute=minutes, 
               second=seconds,
               microsecond=microseconds,
               tzinfo=tz)