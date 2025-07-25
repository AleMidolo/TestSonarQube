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
        raise ValueError("ticks must be in the range 0 <= ticks < 86400000000000")
    
    nanoseconds = ticks % 1000
    microseconds = (ticks // 1000) % 1000
    milliseconds = (ticks // 1000000) % 1000
    seconds = (ticks // 1000000000) % 60
    minutes = (ticks // 60000000000) % 60
    hours = (ticks // 3600000000000) % 24
    
    time_obj = datetime.time(hour=hours, minute=minutes, second=seconds, 
                             microsecond=milliseconds * 1000 + microseconds, 
                             tzinfo=tz)
    
    return time_obj