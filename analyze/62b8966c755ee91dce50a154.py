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
    
    TIMEZONE_PATTERNS = {
        'Z': r'Z',
        'offset': r'(?P<tzoffset_sign>[+-])(?P<tzoffset_hour>\d{2})(?::?(?P<tzoffset_minute>\d{2}))?'
    }

    dt_str = dt_str.strip()

    # Split into date and time parts
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T', 1)
    else:
        date_str = dt_str
        time_str = ''

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
        weekday = int(date_parts.get('weekday', '1'))
        dt = datetime.strptime(f"{year}-{week}-{weekday}", "%Y-%W-%w")
    else:
        # Calendar date
        year = int(date_parts['year'])
        month = int(date_parts.get('month', '1'))
        day = int(date_parts.get('day', '1'))
        dt = datetime(year, month, day)

    # Parse time if present
    if time_str:
        time_parts = re.match(TIME_PATTERN, time_str.split('+')[0].split('-')[0].split('Z')[0])
        if not time_parts:
            raise ValueError("Invalid ISO format time")
            
        time_dict = time_parts.groupdict()
        
        hour = int(time_dict.get('hour', '0'))
        if hour == 24:
            hour = 0
            dt = dt + timedelta(days=1)
            
        minute = int(time_dict.get('minute', '0'))
        second = int(time_dict.get('second', '0'))
        
        microsecond = time_dict.get('microsecond')
        if microsecond:
            microsecond = int(microsecond.ljust(6, '0'))
        else:
            microsecond = 0

        dt = dt.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

        # Parse timezone
        tz = None
        if 'Z' in time_str:
            tz = tzutc()
        else:
            offset_match = re.search(TIMEZONE_PATTERNS['offset'], time_str)
            if offset_match:
                offset_dict = offset_match.groupdict()
                offset_sign = 1 if offset_dict['tzoffset_sign'] == '+' else -1
                offset_hour = int(offset_dict['tzoffset_hour'])
                offset_minute = int(offset_dict.get('tzoffset_minute', '0'))
                offset = offset_sign * timedelta(hours=offset_hour, minutes=offset_minute)
                
                if offset.total_seconds() == 0:
                    tz = tzutc()
                else:
                    tz = tzoffset(None, offset_sign * (offset_hour * 3600 + offset_minute * 60))

        if tz is not None:
            dt = dt.replace(tzinfo=tz)

    return dt