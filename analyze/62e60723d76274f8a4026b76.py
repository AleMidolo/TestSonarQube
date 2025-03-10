from datetime import time, timedelta

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
    seconds_total = ticks // 1000000000
    seconds = seconds_total % 60
    minutes_total = seconds_total // 60
    minutes = minutes_total % 60
    hours = minutes_total // 60
    
    return time(hour=hours, minute=minutes, second=seconds, microsecond=nanoseconds // 1000, tzinfo=tz)