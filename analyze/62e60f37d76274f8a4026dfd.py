def dehydrate_time(value):
    """
    在 Time 类中使用 ticks 来生成 Structure 类。
    用于 `time` 值的转换器。

    :param value: Time 对象
    :type value: Time
    :return: 包含 ticks 的 Structure 对象
    :rtype: Structure
    """
    return Structure(ticks=value.ticks)