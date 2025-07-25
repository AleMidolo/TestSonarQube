def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds:  
    :param tz:  
    :return: Time
    """
    from datetime import datetime, timezone, timedelta

    if tz is None:
        tz = timezone.utc

    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1_000_000_000
    # Create a datetime object in the specified timezone
    time = datetime.fromtimestamp(seconds, tz)
    
    return time