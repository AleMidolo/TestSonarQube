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
        'week_basic': r'(?P<year>\d{4})W(?P<week>\d{2})(?P<day>\d)?',
        'week_extended': r'(?P<year>\d{4})-W(?P<week>\d{2})(?:-(?P<day>\d))?'
    }

    TIME_PATTERN = r'(?P<hour>[0-2]\d)(?::?(?P<minute>\d{2})(?::?(?P<second>\d{2})(?:[.,](?P<microsecond>\d{1,6}))?)?)?' 
    TIMEZONE_PATTERN = r'(?P<tzoffset>Z|[+-]\d{2}(?::?\d{2})?)?$'

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
        day = int(date_parts.get('day', '1'))
        date_obj = datetime.strptime(f"{year}-{week}-{day}", "%Y-%W-%w").date()
        year, month, day = date_obj.year, date_obj.month, date_obj.day
    else:
        year = int(date_parts['year'])
        month = int(date_parts.get('month', '1'))
        day = int(date_parts.get('day', '1'))

    # Initialize time components
    hour = minute = second = microsecond = 0
    tz = None

    # Parse time if present
    if time_str:
        time_match = re.match(TIME_PATTERN + TIMEZONE_PATTERN, time_str)
        if not time_match:
            raise ValueError("Invalid ISO format time")
        
        time_parts = time_match.groupdict()
        
        hour = int(time_parts.get('hour', '0'))
        if hour == 24:  # Special case for midnight
            hour = 0
            
        minute = int(time_parts.get('minute', '0'))
        second = int(time_parts.get('second', '0'))
        
        if time_parts.get('microsecond'):
            microsecond = int(time_parts['microsecond'].ljust(6, '0'))

        # Parse timezone
        tzoffset = time_parts.get('tzoffset')
        if tzoffset:
            if tzoffset == 'Z':
                tz = tzutc()
            else:
                match = re.match(r'([+-])(\d{2})(?::?(\d{2}))?', tzoffset)
                if match:
                    sign, hours, minutes = match.groups()
                    offset = int(hours) * 60 + (int(minutes) if minutes else 0)
                    if sign == '-':
                        offset = -offset
                    tz = tzoffset('', offset * 60)

    return datetime(year, month, day, hour, minute, second, microsecond, tz)