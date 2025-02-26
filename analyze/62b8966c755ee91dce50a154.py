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
    date_patterns = [
        r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',  # YYYY-MM-DD
        r'(?P<year>\d{4})-(?P<week>\d{2})-W(?P<weekday>\d)',  # YYYY-Www-D
        r'(?P<year>\d{4})-(?P<week>\d{2})',  # YYYY-Www
        r'(?P<year>\d{4})',  # YYYY
        r'(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})',  # YYYYMMDD
        r'(?P<year>\d{4})(?P<week>\d{2})W(?P<weekday>\d)',  # YYYYWwwD
        r'(?P<year>\d{4})(?P<week>\d{2})'  # YYYYWww
    ]

    time_patterns = [
        r'(?P<hour>\d{1,2}):(?P<minute>\d{2}):(?P<second>\d{2})(\.(?P<subsecond>\d{1,6}))?',  # hh:mm:ss.ssssss
        r'(?P<hour>\d{1,2}):(?P<minute>\d{2})(\.(?P<subsecond>\d{1,6}))?',  # hh:mm.ssssss
        r'(?P<hour>\d{1,2})(?P<minute>\d{2})(?P<second>\d{2})(\.(?P<subsecond>\d{1,6}))?',  # hhmmss.ssssss
        r'(?P<hour>\d{1,2})(?P<minute>\d{2})(\.(?P<subsecond>\d{1,6}))?',  # hhmm.ssssss
        r'(?P<hour>\d{1,2})'  # hh
    ]

    tz_patterns = [
        r'Z',  # UTC
        r'(?P<sign>[+-])(?P<hour>\d{2}):(?P<minute>\d{2})',  # ±HH:MM
        r'(?P<sign>[+-])(?P<hour>\d{2})(?P<minute>\d{2})',  # ±HHMM
        r'(?P<sign>[+-])(?P<hour>\d{2})'  # ±HH
    ]

    # Combine patterns
    date_regex = re.compile('|'.join(date_patterns))
    time_regex = re.compile('|'.join(time_patterns))
    tz_regex = re.compile('|'.join(tz_patterns))

    # Split date and time
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T', 1)
    else:
        date_str, time_str = dt_str, ''

    # Parse date
    date_match = date_regex.fullmatch(date_str)
    if not date_match:
        raise ValueError(f"Invalid date format: {date_str}")

    year = int(date_match.group('year'))
    month = int(date_match.group('month') or 1)
    day = int(date_match.group('day') or 1)

    # Handle ISO week date
    if date_match.group('week'):
        week = int(date_match.group('week'))
        weekday = int(date_match.group('weekday') or 0)
        if weekday:
            # Calculate the date from ISO week
            first_day_of_year = datetime(year, 1, 1)
            first_weekday = first_day_of_year.isocalendar()[2]
            days_to_first_week = (7 - first_weekday + 1) % 7
            date = first_day_of_year + timedelta(days=days_to_first_week + (week - 1) * 7 + (weekday - 1))
        else:
            date = datetime(year, 1, 1) + timedelta(weeks=week - 1)
    else:
        date = datetime(year, month, day)

    # Parse time
    time_match = time_regex.fullmatch(time_str)
    if time_match:
        hour = int(time_match.group('hour') or 0)
        minute = int(time_match.group('minute') or 0)
        second = int(time_match.group('second') or 0)
        subsecond = int(time_match.group('subsecond') or 0) if time_match.group('subsecond') else 0
        time = datetime(year, month, day, hour, minute, second, subsecond)
    else:
        time = date

    # Parse timezone
    tz_match = tz_regex.fullmatch(dt_str.split('T')[-1]) if 'T' in dt_str else None
    if tz_match:
        if tz_match.group(0) == 'Z':
            tzinfo = tz.tzutc()
        else:
            sign = 1 if tz_match.group('sign') == '+' else -1
            tz_hour = int(tz_match.group('hour'))
            tz_minute = int(tz_match.group('minute') or 0)
            tzinfo = tz.tzoffset(None, sign * (tz_hour * 3600 + tz_minute * 60))
    else:
        tzinfo = None

    # Combine date and time
    if tzinfo:
        return time.replace(tzinfo=tzinfo)
    return time