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
    # 验证时间戳范围
    if not 0 <= ticks < 86400000000000:
        raise ValueError("时间戳必须在0到86400000000000之间")
        
    # 计算时分秒微秒
    microseconds = ticks // 1000  # 转换为微秒
    total_seconds = microseconds // 1000000
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    microseconds = microseconds % 1000000
    
    # 创建时间对象
    return cls(hours, minutes, seconds, microseconds, tzinfo=tz)