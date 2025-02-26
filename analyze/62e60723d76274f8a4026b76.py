def from_ticks(cls, ticks, tz=None):
    """
    टिक से समय बनाएं (आधी रात के बाद से नैनोसेकंड)।

    :param ticks: आधी रात के बाद से नैनोसेकंड
    :type ticks: int
    :param tz: वैकल्पिक टाइमज़ोन
    :type tz: datetime.tzinfo

    :rtype: Time

    :raises ValueError: यदि ticks सीमा से बाहर है
        (0 <= ticks < 86400000000000)
    """
    if not (0 <= ticks < 86400000000000):
        raise ValueError("Ticks must be in the range 0 to 86400000000000.")
    
    from datetime import datetime, timedelta
    
    # Calculate the time from ticks
    midnight = datetime(1, 1, 1, 0, 0, 0, 0, tzinfo=tz)
    time_delta = timedelta(microseconds=ticks / 1000)
    result_time = midnight + time_delta
    
    return result_time.time()