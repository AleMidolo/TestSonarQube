def hydrate_time(nanoseconds, tz=None):
    """
    Hydrator for `Time` and `LocalTime` values.

    :param nanoseconds: The time in nanoseconds to be converted.
    :param tz: Optional timezone information.
    :return: Time
    """
    from datetime import datetime, timezone, timedelta

    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1_000_000_000

    # Create a UTC datetime object
    utc_time = datetime.fromtimestamp(seconds, tz=timezone.utc)

    if tz is not None:
        # Convert to the specified timezone
        local_time = utc_time.astimezone(tz)
        return local_time
    return utc_time