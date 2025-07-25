def isoparse(self, dt_str):
    import datetime
    import re
    from dateutil.tz import tzutc, tzoffset

    # Regular expressions for parsing
    date_regex = r'(?P<year>\d{4})(?:-?(?P<month>\d{2})(?:-?(?P<day>\d{2})|)|)'
    week_regex = r'(?P<year>\d{4})-?W(?P<week>\d{2})(?:-?(?P<weekday>\d)|)'
    time_regex = r'(?P<hour>[0-2]\d)(?::?(?P<minute>\d{2})(?::?(?P<second>\d{2})(?:[.,](?P<microsecond>\d{1,6})\d*)?)?)?'
    tz_regex = r'(?P<tzname>Z|(?P<tzsign>[+-])(?P<tzhour>\d{2})(?::?(?P<tzminute>\d{2})?)?)'

    dt_str = str(dt_str).strip()
    
    # Split into date and time parts
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

    # If no time component, return datetime at midnight
    if not time_str:
        return datetime.datetime(date.year, date.month, date.day)

    # Split time and timezone
    time_parts = re.split('[Z+-]', time_str)
    time_str = time_parts[0]
    tz_str = time_str[len(time_parts[0]):] if len(time_str) > len(time_parts[0]) else ''

    # Parse time
    time_match = re.match(time_regex, time_str)
    if not time_match:
        raise ValueError("Invalid time format")
    
    time_dict = time_match.groupdict()
    hour = int(time_dict['hour'])
    minute = int(time_dict['minute']) if time_dict['minute'] else 0
    second = int(time_dict['second']) if time_dict['second'] else 0
    microsecond = int(time_dict['microsecond'].ljust(6, '0')) if time_dict['microsecond'] else 0

    # Handle special case of 24:00
    if hour == 24:
        if minute != 0 or second != 0 or microsecond != 0:
            raise ValueError("Hour 24 only valid for midnight")
        hour = 0
        date += datetime.timedelta(days=1)

    # Parse timezone
    tz = None
    if tz_str:
        tz_match = re.match(tz_regex, tz_str)
        if not tz_match:
            raise ValueError("Invalid timezone format")
        
        tz_dict = tz_match.groupdict()
        if tz_dict['tzname'] == 'Z':
            tz = tzutc()
        else:
            tz_sign = 1 if tz_dict['tzsign'] == '+' else -1
            tz_hour = int(tz_dict['tzhour'])
            tz_minute = int(tz_dict['tzminute']) if tz_dict['tzminute'] else 0
            
            # Convert to minutes
            offset = tz_sign * (tz_hour * 60 + tz_minute)
            
            if offset == 0:
                tz = tzutc()
            else:
                tz = tzoffset(None, offset * 60)

    return datetime.datetime(date.year, date.month, date.day,
                           hour, minute, second, microsecond, tz)