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
        day = int(date_parts.get('day', '1'))
        date_obj = datetime.strptime(f"{year}-{week}-{day}", "%Y-%W-%w").date()
        year, month, day = date_obj.year, date_obj.month, date_obj.day
    else:
        year = int(date_parts['year'])
        month = int(date_parts.get('month', '1'))
        day = int(date_parts.get('day', '1'))

    # Initialize with date
    dt = datetime(year, month, day)

    # Parse time if present
    if time_str:
        time_match = re.match(TIME_PATTERN + TZ_PATTERN, time_str)
        if not time_match:
            raise ValueError("Invalid ISO format time")
        
        time_parts = time_match.groupdict()
        
        # Handle time components
        hour = int(time_parts.get('hour', '0'))
        if hour == 24:
            hour = 0
            dt = dt + timedelta(days=1)
            
        minute = int(time_parts.get('minute', '0'))
        second = int(time_parts.get('second', '0'))
        
        # Handle microseconds
        microsecond = time_parts.get('microsecond')
        if microsecond:
            microsecond = int(microsecond.ljust(6, '0'))
        else:
            microsecond = 0

        # Handle timezone
        tz = time_parts.get('tzoffset')
        if tz:
            if tz == 'Z':
                tzinfo = tzutc()
            else:
                # Parse timezone offset
                tz_match = re.match(r'([+-])(\d{2})(?::?(\d{2}))?', tz)
                if tz_match:
                    sign, tz_hour, tz_minute = tz_match.groups()
                    offset = int(tz_hour) * 60 + (int(tz_minute) if tz_minute else 0)
                    if sign == '-':
                        offset = -offset
                    tzinfo = tzoffset(None, offset * 60)
                else:
                    raise ValueError("Invalid timezone format")
        else:
            tzinfo = None

        dt = dt.replace(hour=hour, minute=minute, second=second, 
                       microsecond=microsecond, tzinfo=tzinfo)

    return dt