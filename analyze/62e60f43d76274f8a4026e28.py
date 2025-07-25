def hydrate_time(nanoseconds, tz=None):
    """
    将纳秒转换为固定格式的时间。
    用于处理 `Time` 和 `LocalTime` 值的转换器。

    :param nanoseconds: 纳秒时间戳
    :param tz: 时区信息,默认为None
    :return: 格式化的时间字符串
    """
    from datetime import datetime, timezone, timedelta
    
    # 将纳秒转换为秒
    seconds = nanoseconds / 1e9
    
    # 创建datetime对象
    dt = datetime.fromtimestamp(seconds)
    
    # 处理时区
    if tz is not None:
        if isinstance(tz, str):
            # 如果tz是字符串,假设格式为'+/-HH:MM'
            sign = 1 if tz[0] == '+' else -1
            hours = int(tz[1:3])
            minutes = int(tz[4:6])
            offset = timedelta(hours=sign*hours, minutes=sign*minutes)
            tz = timezone(offset)
        dt = dt.astimezone(tz)
    
    # 格式化输出,包含纳秒
    microseconds = int((nanoseconds % 1e9) / 1e3)
    formatted_time = dt.strftime('%H:%M:%S.') + f'{microseconds:06d}'
    
    return formatted_time