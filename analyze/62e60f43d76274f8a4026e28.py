from datetime import datetime, timedelta, timezone

def hydrate_time(nanoseconds, tz=None):
    """
    将纳秒转换为固定格式的时间。
    用于处理 `Time` 和 `LocalTime` 值的转换器。

    :param nanoseconds: 纳秒时间戳
    :param tz: 时区信息，默认为None
    :return: 格式化后的时间字符串
    """
    # 将纳秒转换为秒
    seconds = nanoseconds / 1e9
    # 创建一个UTC时间对象
    dt = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=seconds)
    
    # 如果提供了时区信息，转换为该时区
    if tz is not None:
        dt = dt.astimezone(tz)
    
    # 格式化时间为固定格式
    formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S.%f')
    
    return formatted_time