def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds:  
    :param tz:  
    :return: Time
    """
    from datetime import datetime, timedelta
    import pytz

    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1_000_000_000
    # Create a datetime object from the epoch
    time = datetime(1970, 1, 1) + timedelta(seconds=seconds)

    if tz:
        # If a timezone is provided, localize the time
        timezone = pytz.timezone(tz)
        time = timezone.localize(time)

    return time