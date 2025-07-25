def from_ticks(cls, ticks, tz=None):
    """
    根据时间戳（自午夜以来的纳秒数）创建一个时间对象。

    :param ticks: 自午夜以来的纳秒数
    :type ticks: int
    :param tz: 可选的时区信息
    :type tz: datetime.tzinfo
    :rtype: Time
    :raises ValueError: 如果时间戳超出范围(0 <= ticks < 86400000000000)
    """
    if not (0 <= ticks < 86400000000000):
        raise ValueError("时间戳超出范围(0 <= ticks < 86400000000000)")
    
    seconds = ticks // 1_000_000_000
    nanoseconds = ticks % 1_000_000_000
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    time_obj = cls(hour=hours, minute=minutes, second=seconds, microsecond=nanoseconds // 1000, tzinfo=tz)
    return time_obj