def isoparse(self, dt_str):
    from datetime import datetime, timedelta, date
    from dateutil.tz import tzutc, tzoffset
    import re

    # Regular expressions for parsing
    DATE_PATTERNS = {
        'basic': r'(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})',
        'extended': r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
        'year_only': r'(?P<year>\d{4})',
        'year_month_basic': r'(?P<year>\d{4})(?P<month>\d{2})',
        'year_month_extended': r'(?P<year>\d{4})-(?P<month>\d{2})',
        'week_basic': r'(?P<year>\d{4})W(?P<week>\d{2})(?P<weekday>\d)?',
        'week_extended': r'(?P<year>\d{4})-W(?P<week>\d{2})(?:-(?P<weekday>\d))?'
    }

    TIME_PATTERN = r'(?P<hour>[0-2]\d)(?::?(?P<minute>[0-5]\d)(?::?(?P<second>[0-5]\d)(?:[.,](?P<microsecond>\d{1,6}))?)?)?' 
    TZ_PATTERN = r'(?P<tzoffset>Z|[+-]\d{2}(?::?\d{2})?)?$'

    dt_str = dt_str.strip()

    # Split date and time parts
    parts = re.split('[T ]', dt_str, maxsplit=1)
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

    # Handle week format
    if 'week' in date_parts:
        year = int(date_parts['year'])
        week = int(date_parts['week'])
        weekday = int(date_parts.get('weekday', '1'))
        dt = datetime.strptime(f"{year}-{week}-{weekday}", "%Y-%W-%w")
        year, month, day = dt.year, dt.month, dt.day
    else:
        year = int(date_parts['year'])
        month = int(date_parts.get('month', '1'))
        day = int(date_parts.get('day', '1'))

    # Initialize time components
    hour = minute = second = microsecond = 0
    tz = None

    # Parse time if present
    if time_str:
        time_match = re.match(TIME_PATTERN + TZ_PATTERN, time_str)
        if not time_match:
            raise ValueError("Invalid ISO format time")
        
        time_parts = time_match.groupdict()
        
        # Parse time components
        hour = int(time_parts.get('hour', '0'))
        if hour == 24:  # Special case for midnight
            hour = 0
        minute = int(time_parts.get('minute', '0'))
        second = int(time_parts.get('second', '0'))
        
        # Handle microseconds
        if time_parts.get('microsecond'):
            microsecond = int(time_parts['microsecond'].ljust(6, '0')[:6])

        # Parse timezone
        tzoffset = time_parts.get('tzoffset')
        if tzoffset:
            if tzoffset == 'Z':
                tz = tzutc()
            else:
                # Parse timezone offset
                tz_match = re.match(r'([+-])(\d{2})(?::?(\d{2}))?', tzoffset)
                if tz_match:
                    sign = 1 if tz_match.group(1) == '+' else -1
                    tz_hour = int(tz_match.group(2))
                    tz_minute = int(tz_match.group(3) or '0')
                    offset = sign * (tz_hour * 60 + tz_minute) * 60
                    tz = tzoffset(None, offset)

    return datetime(year, month, day, hour, minute, second, microsecond, tz)