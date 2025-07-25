import datetime

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

    time_units = {
        "seconds": "seconds",
        "second": "seconds",
        "minutes": "minutes",
        "minute": "minutes",
        "hours": "hours",
        "hour": "hours",
        "days": "days",
        "day": "days",
        "weeks": "weeks",
        "week": "weeks",
        "months": "days",  # Approximation: 1 month = 30 days
        "months": "days",  # Approximation: 1 month = 30 days
        "years": "days"    # Approximation: 1 year = 365 days
    }

    parts = frequency.split()
    if len(parts) != 2:
        raise ValueError("Invalid frequency format")

    try:
        value = int(parts[0])
    except ValueError:
        raise ValueError("Invalid number in frequency")

    unit = parts[1].lower()
    if unit not in time_units:
        raise ValueError("Invalid time unit in frequency")

    kwargs = {time_units[unit]: value}
    return datetime.timedelta(**kwargs)