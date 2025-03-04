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
        'year_month': r'(?P<year>\d{4})-?(?P<month>\d{2})',
        'year': r'(?P<year>\d{4})'
    }

    TIME_PATTERN = r'(?P<hour>[0-2]\d)(?::?(?P<minute>[0-5]\d)(?::?(?P<second>[0-5]\d)(?:[.,](?P<microsecond>\d{1,6}))?)?)?' 
    TZ_PATTERN = r'(?P<tzoffset>Z|[+-]\d{2}:?\d{2}|[+-]\d{2})?$'

    # Convert string to datetime components
    def parse_date(date_str):
        for pattern in DATE_PATTERNS.values():
            match = re.match(pattern, date_str)
            if match:
                groups = match.groupdict()
                if 'week' in groups:
                    # Handle ISO week date
                    year = int(groups['year'])
                    week = int(groups['week'])
                    weekday = int(groups.get('weekday', 1))
                    jan1 = date(year, 1, 1)
                    week1 = jan1 + timedelta(days=(8-jan1.isoweekday()))
                    target_date = week1 + timedelta(weeks=week-1, days=weekday-1)
                    return target_date.year, target_date.month, target_date.day
                else:
                    # Handle regular date
                    year = int(groups['year'])
                    month = int(groups.get('month', 1))
                    day = int(groups.get('day', 1))
                    return year, month, day
        raise ValueError("Invalid ISO date format")

    def parse_time(time_str):
        if not time_str:
            return 0, 0, 0, 0
        match = re.match(TIME_PATTERN, time_str)
        if match:
            groups = match.groupdict()
            hour = int(groups.get('hour', 0))
            minute = int(groups.get('minute', 0))
            second = int(groups.get('second', 0))
            microsecond = groups.get('microsecond')
            if microsecond:
                microsecond = int(microsecond.ljust(6, '0'))
            else:
                microsecond = 0
            return hour, minute, second, microsecond
        raise ValueError("Invalid ISO time format")

    def parse_timezone(tz_str):
        if not tz_str:
            return None
        if tz_str == 'Z':
            return tzutc()
        match = re.match(r'([+-])(\d{2}):?(\d{2})?', tz_str)
        if match:
            sign = 1 if match.group(1) == '+' else -1
            hours = int(match.group(2))
            minutes = int(match.group(3) or '0')
            return tzoffset(None, sign * (hours * 3600 + minutes * 60))
        raise ValueError("Invalid timezone format")

    # Split input string into components
    parts = dt_str.split('T' if 'T' in dt_str else ' ', 1)
    date_str = parts[0]
    time_str = parts[1] if len(parts) > 1 else ''

    # Split time and timezone
    time_parts = re.split('[Z+-]', time_str, 1)
    time_str = time_parts[0]
    tz_str = dt_str[-(len(dt_str)-dt_str.rindex(time_parts[0])):] if len(time_parts) > 1 else ''

    # Parse components
    year, month, day = parse_date(date_str)
    hour, minute, second, microsecond = parse_time(time_str)
    tzinfo = parse_timezone(tz_str)

    # Create datetime object
    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo)