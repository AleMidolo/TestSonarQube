import datetime

def from_ticks(cls, ticks, tz=None):
    """
    Create a time from ticks (nanoseconds since midnight).

    :param ticks: nanoseconds since midnight
    :type ticks: int
    :param tz: optional timezone
    :type tz: datetime.tzinfo

    :rtype: Time

    :raises ValueError: if ticks is out of bounds
        (0 <= ticks < 86400000000000)
    """
    if not (0 <= ticks < 86400000000000):
        raise ValueError("ticks must be between 0 and 86400000000000")
    
    nanoseconds = ticks % 1000000000
    seconds = (ticks // 1000000000) % 60
    minutes = (ticks // 60000000000) % 60
    hours = ticks // 3600000000000
    
    time_obj = datetime.time(hour=hours, minute=minutes, second=seconds, microsecond=nanoseconds // 1000, tzinfo=tz)
    return time_obj