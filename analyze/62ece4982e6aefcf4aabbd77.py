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
            raise ValueError("Invalid frequency format. Expected format: 'number timeunit'")
        
        num = int(parts[0])
        timeunit = parts[1].lower()
        
        if timeunit == "weeks":
            return timedelta(weeks=num)
        elif timeunit == "days":
            return timedelta(days=num)
        elif timeunit == "hours":
            return timedelta(hours=num)
        elif timeunit == "minutes":
            return timedelta(minutes=num)
        elif timeunit == "seconds":
            return timedelta(seconds=num)
        elif timeunit == "milliseconds":
            return timedelta(milliseconds=num)
        elif timeunit == "microseconds":
            return timedelta(microseconds=num)
        else:
            raise ValueError(f"Unsupported time unit: {timeunit}")
    
    except ValueError as e:
        raise ValueError(f"Failed to parse frequency: {frequency}. Error: {e}")