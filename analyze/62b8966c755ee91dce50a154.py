def isoparse(self, dt_str):
    from datetime import datetime, timedelta
    from dateutil.tz import tzutc, tzoffset
    import re

    # 基本正则表达式模式
    date_pattern = r"""
        (?P<year>\d{4})
        (?:
            (?:-?(?P<month>\d{2}))
            (?:-?(?P<day>\d{2}))?
            |
            -?W(?P<week>\d{2})
            (?:-?(?P<weekday>\d))?
        )?
    """

    time_pattern = r"""
        (?:T|[\s])?
        (?P<hour>[0-2]\d)
        (?::?(?P<minute>\d{2}))?
        (?::?(?P<second>\d{2}))?
        (?:[.,](?P<microsecond>\d{1,6}))?
    """

    tz_pattern = r"""
        (?P<tz_sign>[+-])
        (?P<tz_hour>\d{2})
        :?(?P<tz_minute>\d{2})?
        |Z
    """

    full_pattern = f"^{date_pattern}(?:{time_pattern})?(?:{tz_pattern})?$"
    
    match = re.match(full_pattern, dt_str.strip(), re.VERBOSE)
    if not match:
        raise ValueError("Invalid ISO format")
        
    parts = match.groupdict()
    
    # 处理日期部分
    year = int(parts['year'])
    month = int(parts.get('month', 1) or 1)
    
    if parts.get('week'):
        # ISO周日期处理
        week = int(parts['week'])
        weekday = int(parts.get('weekday', 1) or 1)
        jan1 = datetime(year, 1, 1)
        week_offset = timedelta(weeks=week-1, days=weekday-1)
        base_date = jan1 + week_offset
        month = base_date.month
        day = base_date.day
    else:
        day = int(parts.get('day', 1) or 1)
    
    # 处理时间部分
    hour = int(parts.get('hour', 0) or 0)
    if hour == 24:  # 处理24:00特殊情况
        hour = 0
        day += 1
        
    minute = int(parts.get('minute', 0) or 0)
    second = int(parts.get('second', 0) or 0)
    
    # 处理微秒
    microsecond = 0
    if parts.get('microsecond'):
        microsecond = int(parts['microsecond'].ljust(6, '0')[:6])
    
    # 处理时区
    tz = None
    if parts.get('tz_sign'):
        tz_hour = int(parts['tz_hour'])
        tz_minute = int(parts.get('tz_minute', 0) or 0)
        offset = tz_hour * 60 + tz_minute
        if parts['tz_sign'] == '-':
            offset = -offset
        if offset == 0:
            tz = tzutc()
        else:
            tz = tzoffset(None, offset * 60)
    elif 'Z' in dt_str:
        tz = tzutc()
        
    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo=tz)