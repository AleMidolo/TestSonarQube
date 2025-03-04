def isoparse(self, dt_str):
    from datetime import datetime, timedelta, date
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
    TIMEZONE_PATTERN = r'(?P<tzname>Z|(?P<tzsign>[+-])(?P<tzhour>\d{2})(?::?(?P<tzminute>\d{2})?)?)?$'

    dt_str = dt_str.strip()
    
    # Split datetime string into date and time parts
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T')
    else:
        if any(c in dt_str for c in ':.-+Z'):  # Contains time components
            date_str, time_str = dt_str.split(' ', 1) if ' ' in dt_str else ('', dt_str)
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
        raise ValueError(f"Invalid ISO format date '{date_str}'")

    # Handle week format
    if 'week' in date_parts:
        year = int(date_parts['year'])
        week = int(date_parts['week'])
        weekday = int(date_parts.get('weekday', '1'))
        date_obj = datetime.strptime(f"{year}-{week}-{weekday}", "%Y-%W-%w").date()
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
            raise ValueError(f"Invalid ISO format time '{time_str}'")

        time_parts = time_match.groupdict()
        
        # Parse time components
        if time_parts.get('hour'):
            hour = int(time_parts['hour'])
            if hour == 24:  # Handle special case of midnight
                hour = 0
                
        if time_parts.get('minute'):
            minute = int(time_parts['minute'])
            
        if time_parts.get('second'):
            second = int(time_parts['second'])
            
        if time_parts.get('microsecond'):
            microsecond = int(time_parts['microsecond'].ljust(6, '0'))

        # Parse timezone
        if time_parts.get('tzname'):
            if time_parts['tzname'] == 'Z':
                tz = tzutc()
            else:
                tzsign = 1 if time_parts['tzsign'] == '+' else -1
                tzhour = int(time_parts['tzhour'])
                tzminute = int(time_parts.get('tzminute', '0'))
                offset = tzsign * (tzhour * 60 + tzminute) * 60
                
                if offset == 0:
                    tz = tzutc()
                else:
                    tz = tzoffset(None, offset)

    # Create and return datetime object
    return datetime(year, month, day, hour, minute, second, microsecond, tz)