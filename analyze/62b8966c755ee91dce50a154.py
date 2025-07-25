def isoparse(self, dt_str):
    from datetime import datetime, timedelta, date
    from dateutil.tz import tzutc, tzoffset
    import re

    # Patrones de expresiones regulares para los diferentes componentes
    DATE_PATTERNS = {
        'full': r'(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})',
        'year_month': r'(?P<year>\d{4})-?(?P<month>\d{2})',
        'year': r'(?P<year>\d{4})',
        'week': r'(?P<year>\d{4})-?W(?P<week>\d{2})(?:-?(?P<weekday>\d))?'
    }

    TIME_PATTERN = r'(?P<hour>[0-2]\d)(?::?(?P<minute>\d{2})(?::?(?P<second>\d{2})(?:[.,](?P<microsecond>\d{1,6}))?)?)?' 
    
    TZ_PATTERN = r'(?P<tzname>Z|(?P<tzsign>[+-])(?P<tzhour>\d{2})(?::?(?P<tzminute>\d{2})?)?)?$'

    dt_str = dt_str.strip()
    
    # Separar fecha y hora
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T')
    else:
        if any(c in dt_str for c in ':.-+Z'):  # Tiene componentes de hora
            date_str, time_str = dt_str.split(' ', 1)
        else:
            date_str, time_str = dt_str, ''

    # Analizar fecha
    date_parts = None
    for pattern_name, pattern in DATE_PATTERNS.items():
        match = re.match(pattern, date_str)
        if match:
            date_parts = match.groupdict()
            break

    if not date_parts:
        raise ValueError("Invalid ISO format date")

    # Convertir fecha
    if 'week' in date_parts:
        year = int(date_parts['year'])
        week = int(date_parts['week'])
        weekday = int(date_parts.get('weekday', '1'))
        dt = datetime.strptime(f"{year}-{week}-{weekday}", "%Y-%W-%w")
    else:
        year = int(date_parts['year'])
        month = int(date_parts.get('month', '1'))
        day = int(date_parts.get('day', '1'))
        dt = datetime(year, month, day)

    # Si no hay hora, retornar
    if not time_str:
        return dt

    # Analizar hora
    time_match = re.match(TIME_PATTERN + TZ_PATTERN, time_str)
    if not time_match:
        raise ValueError("Invalid ISO format time")
    
    time_parts = time_match.groupdict()
    
    # Convertir hora
    hour = int(time_parts.get('hour', '0'))
    if hour == 24:  # Convertir 24:00 a 00:00 del día siguiente
        hour = 0
        dt = dt + timedelta(days=1)
    
    minute = int(time_parts.get('minute', '0'))
    second = int(time_parts.get('second', '0'))
    
    # Manejar microsegundos
    microsecond = time_parts.get('microsecond')
    if microsecond:
        microsecond = int(microsecond.ljust(6, '0'))
    else:
        microsecond = 0

    dt = dt.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

    # Manejar zona horaria
    if time_parts.get('tzname') == 'Z':
        return dt.replace(tzinfo=tzutc())
    elif time_parts.get('tzsign'):
        tzsign = 1 if time_parts['tzsign'] == '+' else -1
        tzhour = int(time_parts['tzhour'])
        tzminute = int(time_parts.get('tzminute', '0'))
        offset = tzsign * (tzhour * 60 + tzminute) * 60
        
        if offset == 0:
            return dt.replace(tzinfo=tzutc())
        return dt.replace(tzinfo=tzoffset(None, offset))

    return dt