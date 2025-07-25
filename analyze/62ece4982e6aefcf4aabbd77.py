from datetime import timedelta

def parse_frequency(frequency):
    """
    给定一个包含数字和时间单位的频率字符串，返回一个对应的 `datetime.timedelta` 实例。

    如果频率为 `None` 或 `"always"`，则返回 `None`。

    如果给定的频率无法解析，则抛出 `ValueError` 异常。

    例如，给定 `"3 timeunit"`，返回 `datetime.timedelta(timeunit=3)`。

    @param frequency : 一个频率字符串，格式为 `"数字 时间单位"`

    @return str, 对应的 `datetime.timedelta` 实例或 `None`
    """
    if frequency is None or frequency == "always":
        return None
        
    try:
        # 分割频率字符串为数字和单位
        number, unit = frequency.split()
        number = int(number)
        
        # 支持的时间单位映射
        units = {
            'days': 'days',
            'day': 'days',
            'weeks': 'weeks', 
            'week': 'weeks',
            'hours': 'hours',
            'hour': 'hours',
            'minutes': 'minutes',
            'minute': 'minutes',
            'seconds': 'seconds',
            'second': 'seconds'
        }
        
        # 检查单位是否支持
        if unit not in units:
            raise ValueError(f"Unsupported time unit: {unit}")
            
        # 构造timedelta参数
        kwargs = {units[unit]: number}
        return timedelta(**kwargs)
        
    except (ValueError, TypeError):
        raise ValueError(f"Invalid frequency format: {frequency}")