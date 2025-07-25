def isoparse(self, dt_str):
    from datetime import datetime, timedelta, date
    from dateutil.tz import tzutc, tzoffset
    import re

    # Regular expressions for parsing
    DATE_PATTERNS = {
        'basic': r'(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})',
        'extended': r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
        'basic_week': r'(?P<year>\d{4})W(?P<week>\d{2})(?P<weekday>\d)?',
        'extended_week': r'(?P<year>\d{4})-W(?P<week>\d{2})(?:-(?P<weekday>\d))?',
        'year_month_basic': r'(?P<year>\d{4})(?P<month>\d{2})',
        'year_month_extended': r'(?P<year>\d{4})-(?P<month>\d{2})',
        'year': r'(?P<year>\d{4})'
    }

    TIME_PATTERN = r'(?P<hour>[0-2]\d)(?::?(?P<minute>[0-5]\d)(?::?(?P<second>[0-5]\d)(?:[.,](?P<microsecond>\d{1,6}))?)?)?' 
    TZ_PATTERN = r'(?P<tzoffset>Z|[+-]\d{2}(?::?\d{2})?)?$'

    # Split date and time parts
    parts = dt_str.split('T' if 'T' in dt_str else ' ', 1)
    date_str = parts[0]
    time_str = parts[1] if len(parts) > 1 else ''

    # Parse date
    date_match = None
    for pattern in DATE_PATTERNS.values():
        match = re.match(pattern + '$', date_str)
        if match:
            date_match = match
            break
    
    if not date_match:
        raise ValueError("Invalid ISO format date")

    date_parts = date_match.groupdict()
    
    # Handle different date formats
    if 'week' in date_parts:
        # ISO week date
        year = int(date_parts['year'])
        week = int(date_parts['week'])
        weekday = int(date_parts.get('weekday', 1))
        temp_date = datetime.strptime(f"{year}-{week}-{weekday}", "%Y-%W-%w").date()
        year, month, day = temp_date.year, temp_date.month, temp_date.day
    else:
        # Standard date
        year = int(date_parts['year'])
        month = int(date_parts.get('month', 1))
        day = int(date_parts.get('day', 1))

    # Parse time if present
    hour = minute = second = microsecond = 0
    tz = None

    if time_str:
        time_match = re.match(TIME_PATTERN + TZ_PATTERN, time_str)
        if not time_match:
            raise ValueError("Invalid ISO format time")
            
        time_parts = time_match.groupdict()
        
        # Parse time components
        hour = int(time_parts.get('hour', 0))
        if hour == 24:
            hour = 0
            
        minute = int(time_parts.get('minute', 0))
        second = int(time_parts.get('second', 0))
        
        if time_parts.get('microsecond'):
            microsecond = int(time_parts['microsecond'].ljust(6, '0'))

        # Parse timezone
        tzoffset_str = time_parts.get('tzoffset')
        if tzoffset_str:
            if tzoffset_str == 'Z':
                tz = tzutc()
            else:
                # Parse timezone offset
                tz_match = re.match(r'([+-])(\d{2})(?::?(\d{2}))?', tzoffset_str)
                if tz_match:
                    sign = 1 if tz_match.group(1) == '+' else -1
                    tz_hour = int(tz_match.group(2))
                    tz_minute = int(tz_match.group(3) or '0')
                    offset = sign * timedelta(hours=tz_hour, minutes=tz_minute)
                    tz = tzoffset(None, offset.total_seconds())

    return datetime(year, month, day, hour, minute, second, microsecond, tz)