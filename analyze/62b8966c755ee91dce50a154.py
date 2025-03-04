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
        # Manejo de fechas basadas en semanas ISO
        year = int(date_parts['year'])
        week = int(date_parts['week'])
        weekday = int(date_parts.get('weekday', '1'))
        date_obj = datetime.strptime(f"{year}-W{week}-{weekday}", "%Y-W%W-%w").date()
        year, month, day = date_obj.year, date_obj.month, date_obj.day
    else:
        year = int(date_parts['year'])
        month = int(date_parts.get('month', '1'))
        day = int(date_parts.get('day', '1'))

    # Valores por defecto para hora
    hour = minute = second = microsecond = 0
    tz = None

    # Analizar hora si existe
    if time_str:
        time_match = re.match(TIME_PATTERN + TZ_PATTERN, time_str)
        if not time_match:
            raise ValueError("Invalid ISO format time")
            
        time_parts = time_match.groupdict()
        
        # Convertir componentes de hora
        hour = int(time_parts.get('hour', '0'))
        if hour == 24:  # Convertir 24:00 a 00:00 del día siguiente
            hour = 0
            day += 1
            
        minute = int(time_parts.get('minute', '0'))
        second = int(time_parts.get('second', '0'))
        
        if time_parts.get('microsecond'):
            # Padding con ceros a la derecha hasta 6 dígitos
            microsecond = int(time_parts['microsecond'].ljust(6, '0'))

        # Procesar zona horaria
        if time_parts.get('tzname') == 'Z':
            tz = tzutc()
        elif time_parts.get('tzsign'):
            tzsign = 1 if time_parts['tzsign'] == '+' else -1
            tzhour = int(time_parts['tzhour'])
            tzminute = int(time_parts.get('tzminute', '0'))
            offset = tzsign * timedelta(hours=tzhour, minutes=tzminute)
            
            if offset.total_seconds() == 0:
                tz = tzutc()
            else:
                tz = tzoffset(None, tzsign * (tzhour * 3600 + tzminute * 60))

    try:
        return datetime(year, month, day, hour, minute, second, microsecond, tzinfo=tz)
    except ValueError as e:
        raise ValueError(f"Invalid date/time components: {e}")