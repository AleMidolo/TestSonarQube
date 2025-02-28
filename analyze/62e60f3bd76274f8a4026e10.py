from datetime import timedelta

def dehydrate_timedelta(value):
    """
    使用 `timedelta` 的值来生成 `Structure` 类。
    用于 `time` 值的转换器。

    :param value: 要转换的 `timedelta` 对象
    :type value: timedelta
    :return: 包含 `days`, `seconds`, `microseconds` 的字典
    :rtype: dict
    """
    if not isinstance(value, timedelta):
        raise TypeError("Expected a timedelta object")
    
    return {
        'days': value.days,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }