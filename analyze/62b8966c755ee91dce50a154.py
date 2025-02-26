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

    # Regular expressions for parsing
    iso_date_regex = re.compile(r'(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?')
    iso_week_regex = re.compile(r'(\d{4})-W(\d{2})(?:-(\d))?')
    time_regex = re.compile(r'(\d{1,2})(?::(\d{2})(?::(\d{2})(?:\.(\d{1,6}))?)?)?')
    tz_regex = re.compile(r'Z|([+-]\d{2}):?(\d{2})?|([+-]\d{2})(\d{2})?|([+-]\d{2})')

    # Split date and time
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T', 1)
    else:
        date_str, time_str = dt_str, ''

    # Parse date
    match = iso_date_regex.match(date_str)
    if match:
        year = int(match.group(1))
        month = int(match.group(2) or 1)
        day = int(match.group(3) or 1)
    else:
        match = iso_week_regex.match(date_str)
        if match:
            year = int(match.group(1))
            week = int(match.group(2))
            day = int(match.group(3) or 1)
            # Calculate the date from ISO week
            first_day_of_year = datetime(year, 1, 1)
            first_weekday = first_day_of_year.weekday()
            days_to_first_monday = (7 - first_weekday) % 7
            first_monday = first_day_of_year + timedelta(days=days_to_first_monday)
            date = first_monday + timedelta(weeks=week - 1, days=day - 1)
            return date.replace(tzinfo=tz.tzutc())
        else:
            raise ValueError("Invalid date format")

    # Parse time
    match = time_regex.match(time_str)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2) or 0)
        second = int(match.group(3) or 0)
        microsecond = int(match.group(4) or 0)
    else:
        hour = minute = second = microsecond = 0

    # Handle midnight case
    if hour == 24:
        hour = 0

    # Create datetime object
    dt = datetime(year, month, day, hour, minute, second, microsecond)

    # Parse timezone
    tz_match = tz_regex.search(dt_str)
    if tz_match:
        if tz_match.group(0) == 'Z':
            dt = dt.replace(tzinfo=tz.tzutc())
        else:
            if tz_match.group(1):
                offset_hours = int(tz_match.group(1))
                offset_minutes = int(tz_match.group(2) or 0)
            elif tz_match.group(3):
                offset_hours = int(tz_match.group(3))
                offset_minutes = 0
            else:
                offset_hours = int(tz_match.group(5))
                offset_minutes = 0
            offset = timedelta(hours=offset_hours, minutes=offset_minutes)
            dt = dt.replace(tzinfo=tz.tzoffset(None, offset.total_seconds()))

    return dt