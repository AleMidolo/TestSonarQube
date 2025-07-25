def isoparse(self, dt_str):
    import datetime
    import re
    from dateutil.tz import tzutc, tzoffset

    # Regular expressions for parsing
    date_regex = r'(?P<year>\d{4})(?:-?(?P<month>\d{2})(?:-?(?P<day>\d{2})|)|)'
    week_regex = r'(?P<year>\d{4})-?W(?P<week>\d{2})(?:-?(?P<weekday>\d)|)'
    time_regex = r'(?P<hour>[0-2]\d)(?::?(?P<minute>\d{2})(?::?(?P<second>\d{2})(?:[.,](?P<microsecond>\d{1,6}))?)?)?' 
    tz_regex = r'(?P<tzname>Z|(?P<tzsign>[+-])(?P<tzhour>\d{2})(?::?(?P<tzminute>\d{2})?)?)?$'

    dt_str = str(dt_str).strip()
    
    # Split date and time parts
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T')
    else:
        if any(c in dt_str for c in ':,.+-Z'):  # If it has time components
            raise ValueError('ISO time format must use T separator')
        date_str, time_str = dt_str, ''

    # Parse date
    date_match = re.match(date_regex, date_str)
    week_match = re.match(week_regex, date_str)
    
    if date_match:
        date_parts = date_match.groupdict()
        year = int(date_parts['year'])
        month = int(date_parts['month'] or 1)
        day = int(date_parts['day'] or 1)
        date = datetime.date(year, month, day)
    elif week_match:
        week_parts = week_match.groupdict()
        year = int(week_parts['year'])
        week = int(week_parts['week'])
        weekday = int(week_parts['weekday'] or 0)
        date = datetime.datetime.strptime(f"{year}-W{week}-{weekday}", "%Y-W%W-%w").date()
    else:
        raise ValueError('Invalid ISO date format')

    # If no time part, return datetime at midnight
    if not time_str:
        return datetime.datetime(date.year, date.month, date.day)

    # Parse time and timezone
    time_parts = re.match(time_regex + tz_regex, time_str)
    if not time_parts:
        raise ValueError('Invalid ISO time format')
    
    parts = time_parts.groupdict()
    
    # Parse time components
    hour = int(parts['hour'])
    if hour == 24:
        hour = 0
    minute = int(parts['minute'] or 0)
    second = int(parts['second'] or 0)
    microsecond = int(parts['microsecond'].ljust(6, '0') if parts['microsecond'] else 0)

    # Parse timezone
    tz = None
    if parts['tzname']:
        if parts['tzname'] == 'Z':
            tz = tzutc()
        else:
            tzsign = 1 if parts['tzsign'] == '+' else -1
            tzhour = int(parts['tzhour'])
            tzminute = int(parts['tzminute'] or 0)
            offset = tzsign * (tzhour * 60 + tzminute) * 60
            if offset == 0:
                tz = tzutc()
            else:
                tz = tzoffset(None, offset)

    return datetime.datetime(date.year, date.month, date.day,
                           hour, minute, second, microsecond, tz)