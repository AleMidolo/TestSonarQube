def isoparse(self, dt_str):
    import datetime
    import re
    from dateutil.tz import tzutc, tzoffset

    # Regular expressions for parsing
    date_regex = r'(?P<year>\d{4})(?:-?(?P<month>\d{2})(?:-?(?P<day>\d{2})|)|)|(?P<yearweek>\d{4})-?W(?P<week>\d{2})(?:-?(?P<weekday>\d)|)'
    time_regex = r'(?P<hour>[0-2]\d)(?::?(?P<minute>\d{2})(?::?(?P<second>\d{2})(?:[.,](?P<microsecond>\d{1,6})\d*)?)?)?'
    tz_regex = r'(?P<tzutc>Z)|(?P<tzhour>[+-]\d{2})(?::?(?P<tzminute>\d{2})?)?'

    dt_str = str(dt_str).strip()
    
    # Split datetime string into date and time parts
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T', 1)
    else:
        date_str = dt_str
        time_str = ''

    # Parse date
    date_match = re.match(date_regex, date_str)
    if not date_match:
        raise ValueError("Invalid ISO-8601 date format")
    
    date_parts = date_match.groupdict()
    
    if date_parts['year']:
        year = int(date_parts['year'])
        month = int(date_parts['month'] or 1)
        day = int(date_parts['day'] or 1)
        date = datetime.date(year, month, day)
    else:
        year = int(date_parts['yearweek'])
        week = int(date_parts['week'])
        weekday = int(date_parts['weekday'] or 0)
        date = datetime.datetime.strptime(f"{year}-W{week}-{weekday}", "%Y-W%W-%w").date()

    # Initialize time components
    hour = minute = second = microsecond = 0
    tz = None

    # Parse time if present
    if time_str:
        # Split time and timezone
        if '+' in time_str:
            time_str, tz_str = time_str.split('+', 1)
            tz_str = '+' + tz_str
        elif '-' in time_str[1:]:  # Avoid splitting on negative hours
            time_str, tz_str = time_str.rsplit('-', 1)
            tz_str = '-' + tz_str
        elif 'Z' in time_str:
            time_str, tz_str = time_str.split('Z', 1)
            tz_str = 'Z'
        else:
            tz_str = ''

        # Parse time components
        time_match = re.match(time_regex, time_str)
        if not time_match:
            raise ValueError("Invalid ISO-8601 time format")
        
        time_parts = time_match.groupdict()
        
        hour = int(time_parts['hour'])
        if hour == 24:  # Special case for midnight
            hour = 0
        minute = int(time_parts['minute'] or 0)
        second = int(time_parts['second'] or 0)
        microsecond = int((time_parts['microsecond'] or '').ljust(6, '0')[:6])

        # Parse timezone if present
        if tz_str:
            if tz_str == 'Z':
                tz = tzutc()
            else:
                tz_match = re.match(tz_regex, tz_str)
                if not tz_match:
                    raise ValueError("Invalid ISO-8601 timezone format")
                
                tz_parts = tz_match.groupdict()
                tz_hour = int(tz_parts['tzhour'])
                tz_minute = int(tz_parts['tzminute'] or 0)
                
                # Convert to minutes offset
                offset = tz_hour * 60 + (tz_minute if tz_hour >= 0 else -tz_minute)
                
                if offset == 0:
                    tz = tzutc()
                else:
                    tz = tzoffset(None, offset * 60)

    return datetime.datetime(date.year, date.month, date.day,
                           hour, minute, second, microsecond, tz)