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
    midnight = datetime.combine(datetime.today(), datetime.min.time())
    time = midnight + timedelta(microseconds=ticks / 1000)

    if tz is not None:
        time = time.astimezone(tz)

    return cls(time)