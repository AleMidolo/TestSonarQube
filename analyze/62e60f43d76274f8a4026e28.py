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

    # If timezone is provided, create timezone object
    if tz is not None:
        if isinstance(tz, int):
            tz = timezone(timedelta(seconds=tz))
        elif isinstance(tz, str):
            # Handle timezone string format like '+01:00'
            hours_offset = int(tz[1:3])
            minutes_offset = int(tz[4:6])
            total_seconds = hours_offset * 3600 + minutes_offset * 60
            if tz[0] == '-':
                total_seconds = -total_seconds
            tz = timezone(timedelta(seconds=total_seconds))

    # Create and return time object
    return time(hour=hours % 24, 
                minute=minutes,
                second=seconds,
                microsecond=microseconds,
                tzinfo=tz)