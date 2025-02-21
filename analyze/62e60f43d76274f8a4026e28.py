def hydrate_time(nanoseconds, tz=None):
    """
    Idratatore per valori di `Time` e `LocalTime`.

    :param nanoseconds:  
    :param tz:  
    :return: Time
    """
    from datetime import datetime, timezone, timedelta

    if tz is None:
        tz = timezone.utc

    seconds = nanoseconds / 1_000_000_000
    dt = datetime.fromtimestamp(seconds, tz)
    return dt