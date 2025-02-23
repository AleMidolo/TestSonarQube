def hydrate_time(nanoseconds, tz=None):
    """
    将纳秒转换为固定格式的时间。
    用于处理 `Time` 和 `LocalTime` 值的转换器。

    :param nanoseconds: 纳秒数
    :param tz: 时区信息，默认为 None
    :return: 格式化的时间字符串
    """
    import datetime
    import pytz

    # 将纳秒转换为秒
    seconds = nanoseconds / 1_000_000_000
    # 创建 UTC 时间
    utc_time = datetime.datetime.utcfromtimestamp(seconds)

    if tz:
        # 如果提供了时区，转换为该时区的时间
        local_tz = pytz.timezone(tz)
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_tz)
    else:
        # 如果没有提供时区，使用 UTC 时间
        local_time = utc_time

    # 返回格式化的时间字符串
    return local_time.strftime('%Y-%m-%d %H:%M:%S %Z')