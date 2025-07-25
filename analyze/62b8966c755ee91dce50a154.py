def isoparse(self, dt_str):
    from datetime import datetime, timedelta
    from dateutil.tz import tzutc, tzoffset
    import re

    # Regular expressions for parsing
    DATE_PATTERNS = {
        'full': r'(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})',
        'year_month': r'(?P<year>\d{4})-?(?P<month>\d{2})',
        'year': r'(?P<year>\d{4})',
        'week': r'(?P<year>\d{4})-?W(?P<week>\d{2})(?:-?(?P<weekday>\d))?'
    }

    TIME_PATTERN = r'(?P<hour>[0-2]\d)(?::?(?P<minute>\d{2})(?::?(?P<second>\d{2})(?:[.,](?P<microsecond>\d{1,6}))?)?)?' 
    TIMEZONE_PATTERN = r'(?P<tzinfo>Z|[+-]\d{2}(?::?\d{2})?)?$'

    dt_str = dt_str.strip()
    
    # Split datetime string into date and time parts
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T')
    else:
        if any(c in dt_str for c in ':.,'):  # Contains time separators
            date_str, time_str = dt_str.split(' ', 1)
        else:
            date_str, time_str = dt_str, ''

    # Parse date
    date_parts = None
    for pattern_name, pattern in DATE_PATTERNS.items():
        match = re.match(pattern + '$', date_str)
        if match:
            date_parts = match.groupdict()
            break
    
    if not date_parts:
        raise ValueError(f"Invalid ISO format date: {date_str}")

    # Convert week format to date if necessary
    if 'week' in date_parts:
        year = int(date_parts['year'])
        week = int(date_parts['week'])
        weekday = int(date_parts.get('weekday', '1'))
        jan1 = datetime(year, 1, 1)
        week_offset = timedelta(weeks=week-1, days=weekday-1)
        base_date = jan1 + week_offset
        date_parts = {
            'year': str(base_date.year),
            'month': str(base_date.month),
            'day': str(base_date.day)
        }

    # Initialize with minimum values
    year = int(date_parts['year'])
    month = int(date_parts.get('month', '1'))
    day = int(date_parts.get('day', '1'))
    hour = minute = second = microsecond = 0
    tz = None

    # Parse time if present
    if time_str:
        time_match = re.match(TIME_PATTERN + TIMEZONE_PATTERN, time_str)
        if not time_match:
            raise ValueError(f"Invalid ISO format time: {time_str}")
        
        time_parts = time_match.groupdict()
        
        # Parse hour (handling special case of 24:00)
        hour = int(time_parts['hour'])
        if hour == 24:
            hour = 0
            day += 1

        # Parse other time components
        if time_parts.get('minute'):
            minute = int(time_parts['minute'])
        if time_parts.get('second'):
            second = int(time_parts['second'])
        if time_parts.get('microsecond'):
            microsecond = int(time_parts['microsecond'].ljust(6, '0'))

        # Parse timezone
        if time_parts.get('tzinfo'):
            tz_str = time_parts['tzinfo']
            if tz_str == 'Z':
                tz = tzutc()
            else:
                # Parse timezone offset
                match = re.match(r'([+-])(\d{2})(?::?(\d{2}))?', tz_str)
                if match:
                    sign, hours, minutes = match.groups()
                    offset = int(hours) * 60 + (int(minutes) if minutes else 0)
                    if sign == '-':
                        offset = -offset
                    if offset == 0:
                        tz = tzutc()
                    else:
                        tz = tzoffset(None, offset * 60)

    try:
        return datetime(year, month, day, hour, minute, second, microsecond, tzinfo=tz)
    except ValueError as e:
        raise ValueError(f"Invalid ISO format datetime: {dt_str}") from e