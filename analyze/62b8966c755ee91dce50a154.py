def isoparse(self, dt_str):
    import datetime
    import re
    from dateutil.tz import tzutc, tzoffset

    # Regular expressions for parsing
    date_regex = r'(?P<year>\d{4})(?:-?(?P<month>\d{2})(?:-?(?P<day>\d{2})|)|)|(?P<isoyear>\d{4})-?W(?P<isoweek>\d{2})(?:-?(?P<isoday>\d{1})|)'
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
        # Handle ISO week dates
        year = int(date_parts['isoyear'])
        week = int(date_parts['isoweek'])
        day = int(date_parts['isoday'] or 1)
        date = datetime.datetime.strptime(f"{year}-W{week}-{day}", "%Y-W%W-%w").date()

    # If no time portion, return datetime at midnight
    if not time_str:
        return datetime.datetime(date.year, date.month, date.day)

    # Split time and timezone
    time_parts = time_str.split('Z', 1)
    has_z = len(time_parts) > 1
    time_str = time_parts[0]

    if not has_z:
        time_parts = re.split('[+-]', time_str, 1)
        time_str = time_parts[0]

    # Parse time
    time_match = re.match(time_regex, time_str)
    if not time_match:
        raise ValueError("Invalid ISO-8601 time format")
    
    time_parts = time_match.groupdict()
    
    hour = int(time_parts['hour'])
    if hour == 24:
        hour = 0
    minute = int(time_parts['minute'] or 0)
    second = int(time_parts['second'] or 0)
    
    microsecond = time_parts['microsecond']
    if microsecond:
        microsecond = int(microsecond.ljust(6, '0'))
    else:
        microsecond = 0

    dt = datetime.datetime(date.year, date.month, date.day,
                         hour, minute, second, microsecond)

    # Parse timezone
    if has_z:
        return dt.replace(tzinfo=tzutc())
    
    if len(time_parts) > 1:
        tz_str = time_str[len(time_parts[0]):]
        tz_match = re.match(tz_regex, tz_str)
        if tz_match:
            tz_parts = tz_match.groupdict()
            if tz_parts['tzutc']:
                return dt.replace(tzinfo=tzutc())
            
            tz_hour = int(tz_parts['tzhour'])
            tz_minute = int(tz_parts['tzminute'] or 0)
            
            offset = tz_hour * 60 + (tz_minute if tz_hour >= 0 else -tz_minute)
            
            # If offset is 0, return UTC
            if offset == 0:
                return dt.replace(tzinfo=tzutc())
            
            return dt.replace(tzinfo=tzoffset(None, offset * 60))

    return dt