from datetime import time, timedelta

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
        raise ValueError("时间戳超出范围 (0 <= ticks < 86400000000000)")
    
    # 将纳秒转换为秒和微秒
    seconds, nanoseconds = divmod(ticks, 1_000_000_000)
    microseconds = nanoseconds // 1000
    
    # 将秒转换为小时、分钟、秒
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # 创建时间对象
    time_obj = time(hour=int(hours), minute=int(minutes), second=int(seconds), microsecond=int(microseconds), tzinfo=tz)
    
    return time_obj