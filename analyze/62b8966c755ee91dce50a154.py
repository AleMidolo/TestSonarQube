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

    TIME_PATTERN = (
        r'(?P<hour>[0-2]\d)(:?(?P<minute>[0-5]\d)(:?(?P<second>[0-5]\d)'
        r'(?:[.,](?P<microsecond>\d{1,6})\d*)?)?)?'
    )

    TZ_PATTERN = r'(?P<tzoffset>Z|[+-]\d{2}:?\d{0,2})'

    # Split date and time parts
    parts = dt_str.split('T' if 'T' in dt_str else ' ', 1)
    date_str = parts[0]
    time_str = parts[1] if len(parts) > 1 else ''

    # Parse date
    date_dict = None
    for pattern in DATE_PATTERNS.values():
        match = re.match(pattern + '$', date_str)
        if match:
            date_dict = match.groupdict()
            break
    
    if not date_dict:
        raise ValueError("Invalid ISO format date")

    # Convert date components
    year = int(date_dict['year'])
    
    if 'month' in date_dict and date_dict['month']:
        month = int(date_dict['month'])
    else:
        month = 1

    if 'week' in date_dict and date_dict['week']:
        # Handle ISO week date format
        week = int(date_dict['week'])
        weekday = int(date_dict.get('weekday', '1'))
        date_obj = datetime.strptime(f"{year}-W{week}-{weekday}", "%Y-W%W-%w").date()
        day = date_obj.day
    elif 'day' in date_dict and date_dict['day']:
        day = int(date_dict['day'])
    else:
        day = 1

    # Parse time if present
    hour = minute = second = microsecond = 0
    tz = None

    if time_str:
        time_parts = re.match(f"{TIME_PATTERN}({TZ_PATTERN})?$", time_str)
        if not time_parts:
            raise ValueError("Invalid ISO format time")
        
        time_dict = time_parts.groupdict()
        
        # Convert time components
        hour = int(time_dict['hour'])
        if hour == 24:  # Special case for midnight
            hour = 0
            
        if time_dict['minute']:
            minute = int(time_dict['minute'])
        
        if time_dict['second']:
            second = int(time_dict['second'])
            
        if time_dict['microsecond']:
            # Pad to 6 digits
            microsecond = int(time_dict['microsecond'].ljust(6, '0'))

        # Handle timezone
        if time_dict.get('tzoffset'):
            tz_str = time_dict['tzoffset']
            if tz_str == 'Z':
                tz = tzutc()
            else:
                # Parse timezone offset
                match = re.match(r'([+-])(\d{2}):?(\d{2})?', tz_str)
                if match:
                    sign, hours, minutes = match.groups()
                    offset = int(hours) * 3600
                    if minutes:
                        offset += int(minutes) * 60
                    if sign == '-':
                        offset = -offset
                    tz = tzoffset(None, offset) if offset != 0 else tzutc()

    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo=tz)