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
    # 检查时间戳范围
    if not 0 <= ticks < 86400000000000:
        raise ValueError("时间戳必须在0到86400000000000之间")
        
    # 计算时分秒和微秒
    nanoseconds = ticks
    microseconds = nanoseconds // 1000
    seconds = microseconds // 1000000
    microseconds = microseconds % 1000000
    
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60

    # 创建时间对象
    return cls(hours, minutes, seconds, microseconds, tz)