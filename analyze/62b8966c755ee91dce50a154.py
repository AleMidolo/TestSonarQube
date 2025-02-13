def isoparse(self, dt_str):
    import re
    from datetime import datetime, timedelta, timezone

    # Define regex patterns for parsing
    date_patterns = [
        r'(\d{4})-(\d{2})-(\d{2})',  # YYYY-MM-DD
        r'(\d{4})-(\d{2})',          # YYYY-MM
        r'(\d{4})',                  # YYYY
        r'(\d{4})W(\d{2})',          # YYYY-Www
        r'(\d{4})W(\d{2})(\d)',      # YYYY-Www-D
    ]
    
    time_patterns = [
        r'(\d{2}):(\d{2}):(\d{2})(\.\d{1,6})?',  # hh:mm:ss.ssssss
        r'(\d{2}):(\d{2})(\.\d{1,6})?',          # hh:mm.ssssss
        r'(\d{2})(:\d{2})?(\.\d{1,6})?',         # hh:mm.ssssss
        r'(\d{2})(\.\d{1,6})?',                  # hh.ssssss
    ]
    
    tz_patterns = [
        r'Z',                                   # UTC
        r'([+-]\d{2}):?(\d{2})?',               # ±HH:MM
        r'([+-]\d{2})(\d{2})?',                  # ±HHMM
        r'([+-]\d{2})'                          # ±HH
    ]
    
    # Combine patterns
    date_regex = re.compile('|'.join(date_patterns))
    time_regex = re.compile('|'.join(time_patterns))
    tz_regex = re.compile('|'.join(tz_patterns))
    
    # Split date and time
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T', 1)
    else:
        date_str, time_str = dt_str, ''
    
    # Parse date
    date_match = date_regex.fullmatch(date_str)
    if not date_match:
        raise ValueError("Invalid date format")
    
    year, month, day, week, week_day = None, None, None, None, None
    if date_match.group(1):  # YYYY-MM-DD
        year, month, day = int(date_match.group(1)), int(date_match.group(2)), int(date_match.group(3))
    elif date_match.group(4):  # YYYY-Www
        year, week = int(date_match.group(1)), int(date_match.group(2))
        day = 1  # Default to first day of the week
    elif date_match.group(5):  # YYYY-Www-D
        year, week, week_day = int(date_match.group(1)), int(date_match.group(2)), int(date_match.group(3))
        day = week_day  # Specific day of the week
    elif date_match.group(6):  # YYYY-MM
        year, month = int(date_match.group(1)), int(date_match.group(2))
        day = 1  # Default to first day of the month
    elif date_match.group(7):  # YYYY
        year = int(date_match.group(1))
        month, day = 1, 1  # Default to first day of the first month
    
    # Parse time
    time_match = time_regex.fullmatch(time_str)
    if time_match:
        hour = int(time_match.group(1) or 0)
        minute = int(time_match.group(2) or 0)
        second = int(time_match.group(3) or 0)
        microsecond = int(float(time_match.group(4) or 0) * 1_000_000) if time_match.group(4) else 0
    else:
        hour, minute, second, microsecond = 0, 0, 0, 0
    
    # Parse timezone
    tz_match = tz_regex.search(dt_str)
    if tz_match:
        tz_str = tz_match.group(0)
        if tz_str == 'Z':
            tz = timezone.utc
        else:
            sign = 1 if tz_str[0] == '+' else -1
            hours = int(tz_str[1:3])
            minutes = int(tz_str[3:5]) if len(tz_str) > 3 else 0
            tz = timezone(timedelta(hours=sign * hours, minutes=sign * minutes))
    else:
        tz = None
    
    # Create datetime object
    if week:
        # Calculate the date from ISO week date
        iso_date = datetime.fromisocalendar(year, week, day)
    else:
        iso_date = datetime(year, month, day)
    
    # Combine date and time
    final_datetime = iso_date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond, tzinfo=tz)
    
    return final_datetime