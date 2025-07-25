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
    
    # 如果指定了时区
    if tz is not None:
        if isinstance(tz, str):
            # 如果时区是字符串格式,创建timezone对象
            try:
                hours = int(tz[1:3])
                minutes = int(tz[3:]) if len(tz) > 3 else 0
                sign = 1 if tz[0] == '+' else -1
                tz = timezone(timedelta(hours=sign*hours, minutes=minutes))
            except:
                raise ValueError("Invalid timezone format")
        dt = dt.astimezone(tz)
    
    # 格式化输出,包含纳秒
    microseconds = int((nanoseconds % 1e9) / 1e3)
    time_str = dt.strftime('%H:%M:%S.{:06d}'.format(microseconds))
    
    if tz is not None:
        # 添加时区信息
        time_str += dt.strftime('%z')
        
    return time_str