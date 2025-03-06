import datetime

def from_ticks(cls, ticks, tz=None):
    """
    टिक से समय बनाएं (आधी रात के बाद से नैनोसेकंड)।

    :param ticks: आधी रात के बाद से नैनोसेकंड
    :type ticks: int
    :param tz: वैकल्पिक टाइमज़ोन
    :type tz: datetime.tzinfo

    :rtype: datetime.time

    :raises ValueError: यदि ticks सीमा से बाहर है
        (0 <= ticks < 86400000000000)
    """
    if not (0 <= ticks < 86400000000000):
        raise ValueError("ticks must be in the range [0, 86400000000000)")
    
    nanoseconds_per_second = 1_000_000_000
    seconds_per_day = 86400
    
    total_seconds = ticks // nanoseconds_per_second
    nanoseconds = ticks % nanoseconds_per_second
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    time_obj = datetime.time(hour=hours, minute=minutes, second=seconds, microsecond=nanoseconds // 1000, tzinfo=tz)
    
    return time_obj