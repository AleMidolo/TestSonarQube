from datetime import datetime, timedelta, timezone

def hydrate_time(nanoseconds, tz=None):
    """
    将纳秒转换为固定格式的时间。
    用于处理 `Time` 和 `LocalTime` 值的转换器。

    :param nanoseconds: 纳秒数
    :param tz: 时区信息，默认为 None
    :return: 格式化的时间字符串
    """
    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1_000_000_000
    # Create a datetime object from the epoch
    dt = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=seconds)
    
    # If a timezone is provided, localize the datetime
    if tz:
        dt = dt.astimezone(tz)
    
    # Return the formatted time string
    return dt.strftime('%Y-%m-%d %H:%M:%S.%f')