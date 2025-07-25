from datetime import time, timedelta, timezone

def hydrate_time(nanoseconds, tz=None):
    """
    Hydrator for `Time` and `LocalTime` values.

    :param nanoseconds: The number of nanoseconds since midnight.
    :param tz: The timezone to apply (optional).
    :return: A `time` object representing the given nanoseconds.
    """
    # Convert nanoseconds to seconds and microseconds
    seconds, nanoseconds = divmod(nanoseconds, 1_000_000_000)
    microseconds = nanoseconds // 1_000
    
    # Create a timedelta representing the time since midnight
    delta = timedelta(seconds=seconds, microseconds=microseconds)
    
    # Create a time object from the timedelta
    t = (time.min + delta).time()
    
    # Apply timezone if provided
    if tz is not None:
        t = t.replace(tzinfo=timezone(tz))
    
    return t