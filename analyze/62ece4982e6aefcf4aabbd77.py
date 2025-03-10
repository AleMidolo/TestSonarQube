from datetime import timedelta

def parse_frequency(frequency):
    """
    给定一个包含数字和时间单位的频率字符串，返回一个对应的 `datetime.timedelta` 实例。

    如果频率为 `None` 或 `"always"`，则返回 `None`。

    如果给定的频率无法解析，则抛出 `ValueError` 异常。

    例如，给定 `"3 timeunit"`，返回 `datetime.timedelta(timeunit=3)`。

    @param frequency : 一个频率字符串，格式为 `"数字 时间单位"`

    @return str, 对应的 `datetime.timedelta` 实例或 `None`

    给定一个包含数字和时间单位的频率字符串，返回一个对应的 `datetime.timedelta` 实例，在频率为 `None` 或 `"always"` 时返回 `None`。

    例如，给定 `"3 weeks"`，返回 `datetime.timedelta(weeks=3)`。

    如果给定的频率无法解析，则抛出 `ValueError` 异常。
    """
    if frequency is None or frequency.lower() == "always":
        return None
    
    try:
        parts = frequency.strip().split()
        if len(parts) != 2:
            raise ValueError("Invalid frequency format")
        
        num = int(parts[0])
        unit = parts[1].lower()
        
        if unit in ['days', 'day', 'd']:
            return timedelta(days=num)
        elif unit in ['weeks', 'week', 'w']:
            return timedelta(weeks=num)
        elif unit in ['hours', 'hour', 'h']:
            return timedelta(hours=num)
        elif unit in ['minutes', 'minute', 'min', 'm']:
            return timedelta(minutes=num)
        elif unit in ['seconds', 'second', 'sec', 's']:
            return timedelta(seconds=num)
        else:
            raise ValueError("Unsupported time unit")
    
    except (ValueError, IndexError):
        raise ValueError("Invalid frequency format")