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
            # 如果tz是字符串,假设是UTC偏移量格式如'+08:00'
            offset = int(tz[1:3]) * 3600 + int(tz[4:6]) * 60
            if tz[0] == '-':
                offset = -offset
            tz = timezone(timedelta(seconds=offset))
        dt = dt.astimezone(tz)
    
    # 格式化输出,包含纳秒精度
    microseconds = int((nanoseconds % 1e9) / 1e3)
    time_str = dt.strftime('%H:%M:%S.{:06d}'.format(microseconds))
    
    return time_str