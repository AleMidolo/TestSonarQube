from datetime import timedelta

class Structure:
    def __init__(self, days=0, seconds=0, microseconds=0):
        self.days = days
        self.seconds = seconds
        self.microseconds = microseconds

def dehydrate_timedelta(value):
    """
    使用 `timedelta` 的值来生成 `Structure` 类。
    用于 `time` 值的转换器。

    :param value: 
    :type value: timedelta
    :return: 
    """
    if not isinstance(value, timedelta):
        raise ValueError("The value must be an instance of timedelta.")
    
    return Structure(days=value.days, seconds=value.seconds, microseconds=value.microseconds)