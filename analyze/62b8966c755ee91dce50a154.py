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
    
    TIMEZONE_PATTERN = r'(?P<tzname>Z|(?P<tzsign>[+-])(?P<tzhour>\d{2})(?::?(?P<tzminute>\d{2})?)?)?$'

    # Combinar los patrones
    patterns = []
    for date_pat in DATE_PATTERNS.values():
        pattern = f'^{date_pat}(?:T{TIME_PATTERN})?{TIMEZONE_PATTERN}'
        patterns.append(re.compile(pattern))

    # Intentar hacer coincidir con cada patrón
    match = None
    for pattern in patterns:
        match = pattern.match(dt_str)
        if match:
            break
    
    if not match:
        raise ValueError(f"Time data '{dt_str}' does not match ISO format")

    # Extraer los componentes
    parts = match.groupdict()

    # Procesar fecha
    year = int(parts.get('year'))
    
    if 'month' in parts and parts['month']:
        month = int(parts['month'])
    else:
        month = 1

    if 'day' in parts and parts['day']:
        day = int(parts['day'])
    else:
        day = 1

    if 'week' in parts and parts['week']:
        # Manejar formato de semana ISO
        week = int(parts['week'])
        weekday = int(parts.get('weekday', 1))
        temp_date = date(year, 1, 4)  # El 4 de enero siempre está en la semana 1
        temp_date = temp_date + timedelta(weeks=week-1, days=weekday-1)
        month, day = temp_date.month, temp_date.day

    # Procesar hora
    hour = int(parts.get('hour', 0))
    if hour == 24:
        hour = 0
        day += 1

    minute = int(parts.get('minute', 0))
    second = int(parts.get('second', 0))
    
    # Procesar microsegundos
    microsecond = 0
    if parts.get('microsecond'):
        microsecond = int(parts['microsecond'].ljust(6, '0')[:6])

    # Procesar zona horaria
    tz = None
    if parts.get('tzname'):
        if parts['tzname'] == 'Z':
            tz = tzutc()
        else:
            tzsign = 1 if parts['tzsign'] == '+' else -1
            tzhour = int(parts['tzhour'])
            tzminute = int(parts.get('tzminute', 0))
            offset = tzsign * (tzhour * 60 + tzminute) * 60
            
            if offset == 0:
                tz = tzutc()
            else:
                tz = tzoffset(None, offset)

    return datetime(year, month, day, hour, minute, second, microsecond, tz)