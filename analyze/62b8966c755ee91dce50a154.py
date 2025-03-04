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
        (?P<tz_sign>[+-])?
        (?P<tz_hour>\d{2})?
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
    
    if parts['month']:
        month = int(parts['month'])
        day = int(parts['day'] or 1)
    elif parts['week']:
        # ISO周处理
        week = int(parts['week'])
        weekday = int(parts['weekday'] or 1)
        jan1 = datetime(year, 1, 1)
        week_offset = timedelta(weeks=week-1, days=weekday-1)
        temp_date = jan1 + week_offset
        month = temp_date.month
        day = temp_date.day
    else:
        month = 1
        day = 1

    # 处理时间部分
    hour = int(parts['hour'] or 0)
    if hour == 24:  # 处理24:00特殊情况
        hour = 0
        day += 1
        
    minute = int(parts['minute'] or 0)
    second = int(parts['second'] or 0)
    
    # 处理微秒
    microsecond = 0
    if parts['microsecond']:
        microsecond = int(parts['microsecond'].ljust(6, '0')[:6])

    # 处理时区
    tz = None
    if parts.get('tz_sign') or 'Z' in dt_str:
        if 'Z' in dt_str:
            tz = tzutc()
        else:
            tz_hour = int(parts['tz_hour'] or 0)
            tz_minute = int(parts['tz_minute'] or 0)
            offset = tz_hour * 60 + tz_minute
            if parts['tz_sign'] == '-':
                offset = -offset
            if offset == 0:
                tz = tzutc()
            else:
                tz = tzoffset(None, offset * 60)

    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo=tz)