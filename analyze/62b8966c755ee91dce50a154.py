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
    
    # Split datetime string into date and time parts
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T')
    else:
        date_str = dt_str
        time_str = ''

    # Parse date
    date_match = re.match(date_regex, date_str)
    week_match = re.match(week_regex, date_str) if not date_match else None
    
    if date_match:
        date_dict = date_match.groupdict()
        year = int(date_dict['year'])
        month = int(date_dict['month']) if date_dict['month'] else 1
        day = int(date_dict['day']) if date_dict['day'] else 1
        date = datetime.date(year, month, day)
    elif week_match:
        date_dict = week_match.groupdict()
        year = int(date_dict['year'])
        week = int(date_dict['week'])
        weekday = int(date_dict['weekday']) if date_dict['weekday'] else 1
        date = datetime.datetime.strptime(f"{year}-W{week}-{weekday}", "%Y-W%W-%w").date()
    else:
        raise ValueError("Invalid ISO format")

    if not time_str:
        return datetime.datetime(date.year, date.month, date.day)

    # Parse time
    time_match = re.match(time_regex + tz_regex, time_str)
    if not time_match:
        raise ValueError("Invalid time format")

    time_dict = time_match.groupdict()
    
    hour = int(time_dict['hour'])
    if hour == 24:
        hour = 0
    minute = int(time_dict['minute']) if time_dict['minute'] else 0
    second = int(time_dict['second']) if time_dict['second'] else 0
    
    microsecond = 0
    if time_dict['microsecond']:
        microsecond = int(time_dict['microsecond'].ljust(6, '0'))

    # Parse timezone
    tz = None
    if time_dict['tzname']:
        if time_dict['tzname'] == 'Z':
            tz = tzutc()
        else:
            tzsign = 1 if time_dict['tzsign'] == '+' else -1
            tzhour = int(time_dict['tzhour'])
            tzminute = int(time_dict['tzminute']) if time_dict['tzminute'] else 0
            offset = tzsign * (tzhour * 60 + tzminute) * 60
            if offset == 0:
                tz = tzutc()
            else:
                tz = tzoffset(None, offset)

    return datetime.datetime(date.year, date.month, date.day,
                           hour, minute, second, microsecond, tz)