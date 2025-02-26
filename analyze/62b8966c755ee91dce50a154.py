def isoparse(self, dt_str):
    """
    将 ISO-8601 格式的日期时间字符串解析为 :class:`datetime.datetime`。

    一个 ISO-8601 日期时间字符串由日期部分组成，后面可选跟随一个时间部分——日期和时间部分之间由单个字符分隔，在官方标准中该字符为 ``T``。不完整的日期格式（例如 ``YYYY-MM``）*不能*与时间部分组合使用。

    支持的日期格式包括：

    常见：

    - ``YYYY``
    - ``YYYY-MM`` 或 ``YYYYMM``
    - ``YYYY-MM-DD`` 或 ``YYYYMMDD``

    不常见：

    - ``YYYY-Www`` 或 ``YYYYWww`` - ISO 周（天数默认为 0）
    - ``YYYY-Www-D`` 或 ``YYYYWwwD`` - ISO 周和天数

    ISO 周和天数的编号逻辑与 :func:`datetime.date.isocalendar` 相同。

    支持的时间格式包括：

    - ``hh``
    - ``hh:mm`` 或 ``hhmm``
    - ``hh:mm:ss`` 或 ``hhmmss``
    - ``hh:mm:ss.ssssss``（最多可包含 6 位子秒数字）

    对于 `hh`，午夜是一个特殊情况，因为标准同时支持用 00:00 和 24:00 表示午夜。小数点分隔符可以是点（``.``）或逗号（``,``）。

    .. caution::

      虽然 ISO-8601 标准支持秒以外的其他小数组件，但当前的解析器尚未实现此功能。

    支持的时区偏移格式包括：

    - ``Z``（UTC）
    - ``±HH:MM``
    - ``±HHMM``
    - ``±HH``

    偏移量将表示为 :class:`dateutil.tz.tzoffset` 对象，UTC 除外，UTC 会表示为 :class:`dateutil.tz.tzutc`。与 UTC 等效的时区偏移（例如 ``+00:00``）也将表示为 :class:`dateutil.tz.tzutc`。

    :param dt_str:
      仅包含一个 ISO-8601 日期时间字符串的字符串或流。

    :return:
      返回一个 :class:`datetime.datetime` 对象，表示该字符串。未指定的组件默认为其最小值。

    .. warning::

      从 2.7.0 版本开始，解析器的严格性不应被视为稳定的契约部分。任何符合 ISO-8601 且在默认设置下能正确解析的字符串，在将来的版本中都能继续正确解析，但当前无法解析的无效字符串（如 ``2017-01-01T00:00+00:00:00``）若在编码上是有效日期，则不保证将来版本会继续无法解析。

    .. versionadded:: 2.7.0
    """
    from datetime import datetime, timedelta
    import re
    from dateutil import tz

    # Define regex patterns for parsing
    date_pattern = r'(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?'
    week_pattern = r'(\d{4})-W(\d{2})(?:-?(\d{1}))?'
    time_pattern = r'(\d{2})(?::(\d{2})(?::(\d{2})(?:\.(\d{1,6}))?)?)?'
    offset_pattern = r'Z|([+-]\d{2}):?(\d{2})?|([+-]\d{2})(\d{2})?|([+-]\d{2})'

    # Combine patterns for full ISO-8601 parsing
    full_pattern = re.compile(
        rf'^{date_pattern}(?:[T ]{time_pattern})?(?:{offset_pattern})?$'
    )

    match = full_pattern.match(dt_str)
    if not match:
        raise ValueError(f"Invalid ISO-8601 date string: {dt_str}")

    # Extract date components
    year, month, day = match.group(1), match.group(2), match.group(3)
    if month is None:
        month = 1
    if day is None:
        day = 1

    # Handle week date if applicable
    if match.group(4):
        week, week_day = match.group(5), match.group(6)
        week = int(week)
        week_day = int(week_day) if week_day else 0
        date = datetime.fromisocalendar(week, week, week_day)
    else:
        date = datetime(int(year), int(month), int(day))

    # Extract time components
    hour, minute, second, microsecond = match.group(7), match.group(8), match.group(9), match.group(10)
    if hour is None:
        hour = 0
    if minute is None:
        minute = 0
    if second is None:
        second = 0
    if microsecond is None:
        microsecond = 0
    else:
        microsecond = int(microsecond.ljust(6, '0'))  # Pad microseconds

    # Create datetime object
    date = date.replace(hour=int(hour), minute=int(minute), second=int(second), microsecond=microsecond)

    # Handle timezone offset
    tz_offset = match.group(11) or match.group(12) or match.group(13)
    if tz_offset == 'Z':
        date = date.replace(tzinfo=tz.tzutc())
    elif tz_offset:
        if match.group(11):
            offset_hours, offset_minutes = int(match.group(12)), int(match.group(13))
            offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        else:
            offset_hours = int(match.group(14))
            offset = timedelta(hours=offset_hours)
        date = date.replace(tzinfo=tz.tzoffset(None, offset.total_seconds()))

    return date