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
    date_components = None
    for pattern_name, pattern in DATE_PATTERNS.items():
        match = re.match(pattern + '$', date_str)
        if match:
            groups = match.groupdict()
            if pattern_name == 'week':
                # Handle ISO week dates
                year = int(groups['year'])
                week = int(groups['week'])
                weekday = int(groups.get('weekday', '1'))
                date_components = date.fromisocalendar(year, week, weekday)
            else:
                year = int(groups['year'])
                month = int(groups.get('month', '1'))
                day = int(groups.get('day', '1'))
                date_components = date(year, month, day)
            break
    
    if date_components is None and date_str:
        raise ValueError(f"Invalid ISO format date '{date_str}'")
    
    if not time_str:
        return datetime.combine(date_components or date(1, 1, 1), datetime.min.time())

    # Parse time
    time_match = re.match(TIME_PATTERN + TIMEZONE_PATTERN, time_str)
    if not time_match:
        raise ValueError(f"Invalid ISO format time '{time_str}'")

    groups = time_match.groupdict()
    
    # Handle special case of hour 24
    hour = int(groups['hour'])
    if hour == 24:
        if any(groups.get(k) not in (None, '00') for k in ['minute', 'second', 'microsecond']):
            raise ValueError("Hour 24 only valid with 0 minutes and seconds")
        hour = 0
        if date_components:
            date_components += timedelta(days=1)
    
    minute = int(groups.get('minute', '0'))
    second = int(groups.get('second', '0'))
    
    # Handle microseconds
    microsecond = groups.get('microsecond')
    if microsecond:
        microsecond = int(microsecond.ljust(6, '0'))
    else:
        microsecond = 0

    # Handle timezone
    tz = None
    if groups['tzname'] is not None:
        if groups['tzname'] == 'Z':
            tz = tzutc()
        else:
            tzsign = 1 if groups['tzsign'] == '+' else -1
            tzhour = int(groups['tzhour'])
            tzminute = int(groups.get('tzminute', '0'))
            
            offset = tzsign * timedelta(hours=tzhour, minutes=tzminute)
            
            # Convert zero offset to UTC
            if offset == timedelta(0):
                tz = tzutc()
            else:
                tz = tzoffset(None, tzsign * (tzhour * 3600 + tzminute * 60))

    return datetime(
        date_components.year if date_components else 1,
        date_components.month if date_components else 1,
        date_components.day if date_components else 1,
        hour, minute, second, microsecond, tz
    )