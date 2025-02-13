from datetime import datetime, timedelta
import re
from dateutil import tz

def isoparse(self, dt_str):
    # Define regex patterns for different ISO-8601 formats
    date_patterns = [
        r'(?P<year>\d{4})',
        r'(?P<year>\d{4})-(?P<month>\d{2})',
        r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
        r'(?P<year>\d{4})-W(?P<week>\d{2})',
        r'(?P<year>\d{4})-W(?P<week>\d{2})-(?P<day>\d{1})'
    ]
    
    time_patterns = [
        r'(?P<hour>\d{2})',
        r'(?P<hour>\d{2}):(?P<minute>\d{2})',
        r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})',
        r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})(?P<fraction>\.\d{1,6})?'
    ]
    
    tz_patterns = [
        r'Z',
        r'(?P<offset_sign>[+-])(?P<offset_hour>\d{2}):?(?P<offset_minute>\d{2})?',
        r'(?P<offset_sign>[+-])(?P<offset_hour>\d{2})(?P<offset_minute>\d{2})?',
        r'(?P<offset_sign>[+-])(?P<offset_hour>\d{2})'
    ]
    
    # Combine patterns
    full_pattern = r'^(?P<date>' + '|'.join(date_patterns) + r')' + \
                   r'(T(?P<time>' + '|'.join(time_patterns) + r')(?P<tz>' + '|'.join(tz_patterns) + r')?)?$'
    
    match = re.match(full_pattern, dt_str)
    if not match:
        raise ValueError("Invalid ISO-8601 string")
    
    date_parts = match.group('date')
    time_parts = match.group('time')
    tz_part = match.group('tz')
    
    # Parse date
    if 'W' in date_parts:
        year = int(match.group('year'))
        week = int(match.group('week'))
        day = int(match.group('day') or 1)
        date = datetime.strptime(f'{year}-W{week}-{day}', "%Y-W%W-%w").date()
    else:
        year = int(match.group('year'))
        month = int(match.group('month') or 1)
        day = int(match.group('day') or 1)
        date = datetime(year, month, day).date()
    
    # Parse time
    if time_parts:
        hour = int(match.group('hour'))
        minute = int(match.group('minute') or 0)
        second = int(match.group('second') or 0)
        microsecond = int(float(match.group('fraction') or 0) * 1_000_000)
        time = datetime.combine(date, datetime.min.time()).replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
    else:
        time = datetime.combine(date, datetime.min.time())
    
    # Parse timezone
    if tz_part:
        if tz_part == 'Z':
            tzinfo = tz.tzutc()
        else:
            offset_sign = match.group('offset_sign')
            offset_hour = int(match.group('offset_hour'))
            offset_minute = int(match.group('offset_minute') or 0)
            total_offset = timedelta(hours=offset_hour, minutes=offset_minute)
            if offset_sign == '-':
                total_offset = -total_offset
            tzinfo = tz.tzoffset(None, total_offset.total_seconds())
    else:
        tzinfo = None
    
    # Combine date and time
    result = time.replace(tzinfo=tzinfo)
    return result