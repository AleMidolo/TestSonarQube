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

    # Eliminar la T entre fecha y hora si existe
    dt_str = dt_str.replace('T', ' ').strip()

    # Separar fecha y hora
    parts = dt_str.split()
    date_str = parts[0]
    time_str = parts[1] if len(parts) > 1 else ''

    # Analizar la fecha
    date_match = None
    for pattern in DATE_PATTERNS.values():
        match = re.match(pattern, date_str)
        if match:
            date_match = match
            break

    if not date_match:
        raise ValueError("Invalid ISO format date")

    date_parts = date_match.groupdict()

    # Manejar fechas basadas en semanas ISO
    if 'week' in date_parts:
        year = int(date_parts['year'])
        week = int(date_parts['week'])
        weekday = int(date_parts.get('weekday', '1'))
        jan1 = date(year, 1, 1)
        week_1 = jan1 + timedelta(days=(8 - jan1.isoweekday()))
        result_date = week_1 + timedelta(weeks=week-1, days=weekday-1)
        year, month, day = result_date.year, result_date.month, result_date.day
    else:
        year = int(date_parts['year'])
        month = int(date_parts.get('month', 1))
        day = int(date_parts.get('day', 1))

    # Valores por defecto para hora
    hour = minute = second = microsecond = 0
    tz = None

    # Analizar la hora si existe
    if time_str:
        time_match = re.match(TIME_PATTERN + TIMEZONE_PATTERN, time_str)
        if not time_match:
            raise ValueError("Invalid ISO format time")
        
        time_parts = time_match.groupdict()
        
        hour = int(time_parts.get('hour', 0))
        if hour == 24:  # Convertir 24:00 a 00:00 del día siguiente
            hour = 0
            day += 1
            
        minute = int(time_parts.get('minute', 0))
        second = int(time_parts.get('second', 0))
        microsecond = int((time_parts.get('microsecond') or '').ljust(6, '0'))

        # Analizar zona horaria
        if time_parts.get('tzname'):
            if time_parts['tzname'] == 'Z':
                tz = tzutc()
            else:
                tzsign = 1 if time_parts['tzsign'] == '+' else -1
                tzhour = int(time_parts['tzhour'])
                tzminute = int(time_parts.get('tzminute', 0))
                offset = tzsign * (tzhour * 60 + tzminute) * 60
                if offset == 0:
                    tz = tzutc()
                else:
                    tz = tzoffset(None, offset)

    return datetime(year, month, day, hour, minute, second, microsecond, tz)