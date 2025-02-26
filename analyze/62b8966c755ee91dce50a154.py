def isoparse(self, dt_str):
    """
    Parse una cadena de fecha y hora en formato ISO-8601 a un objeto :class:`datetime.datetime`.

    Una cadena de fecha y hora en formato ISO-8601 consiste en una parte de fecha, seguida opcionalmente por una parte de hora. Las partes de fecha y hora están separadas por un único carácter separador, que es ``T`` según el estándar oficial. Los formatos de fecha incompletos (como ``YYYY-MM``) *no* pueden combinarse con una parte de hora.

    Los formatos de fecha admitidos son:

    Comunes:

    - ``YYYY``
    - ``YYYY-MM`` o ``YYYYMM``
    - ``YYYY-MM-DD`` o ``YYYYMMDD``

    Poco comunes:

    - ``YYYY-Www`` o ``YYYYWww`` - Semana ISO (el día por defecto es 0)
    - ``YYYY-Www-D`` o ``YYYYWwwD`` - Semana y día ISO

    La numeración de semanas y días ISO sigue la misma lógica que
    :func:`datetime.date.isocalendar`.

    Los formatos de hora admitidos son:

    - ``hh``
    - ``hh:mm`` o ``hhmm``
    - ``hh:mm:ss`` o ``hhmmss``
    - ``hh:mm:ss.ssssss`` (Hasta 6 dígitos para subsegundos)

    La medianoche es un caso especial para `hh`, ya que el estándar admite tanto 00:00 como 24:00 como representación. El separador decimal puede ser un punto o una coma.

    .. precaución::

        El soporte para componentes fraccionarios distintos de los segundos es parte del estándar ISO-8601, pero actualmente no está implementado en este analizador.

    Los formatos de zona horaria admitidos son:

    - `Z` (UTC)
    - `±HH:MM`
    - `±HHMM`
    - `±HH`

    Los desplazamientos se representarán como objetos :class:`dateutil.tz.tzoffset`, con la excepción de UTC, que se representará como :class:`dateutil.tz.tzutc`. Los desplazamientos de zona horaria equivalentes a UTC (como `+00:00`) también se representarán como :class:`dateutil.tz.tzutc`.

    :param dt_str:
        Una cadena o flujo que contiene únicamente una cadena de fecha y hora en formato ISO-8601.

    :return:
        Devuelve un objeto :class:`datetime.datetime` que representa la cadena.
        Los componentes no especificados se inicializan con su valor más bajo.

    .. advertencia::

        A partir de la versión 2.7.0, la rigurosidad del analizador no debe considerarse una parte estable del contrato. Cualquier cadena válida en formato ISO-8601 que se analice correctamente con la configuración predeterminada continuará analizándose correctamente en versiones futuras, pero las cadenas no válidas que actualmente fallan (por ejemplo, ``2017-01-01T00:00+00:00:00``) no están garantizadas para seguir fallando en versiones futuras si codifican una fecha válida.

    .. versión añadida:: 2.7.0
    """
    from datetime import datetime, timedelta
    import re
    from dateutil import tz

    # Regex patterns for parsing
    date_patterns = [
        r'(\d{4})-(\d{2})-(\d{2})',  # YYYY-MM-DD
        r'(\d{4})-(\d{2})',          # YYYY-MM
        r'(\d{4})',                   # YYYY
        r'(\d{4})W(\d{2})',           # YYYY-Www
        r'(\d{4})W(\d{2})-(\d)',      # YYYY-Www-D
    ]
    
    time_patterns = [
        r'(\d{2}):(\d{2}):(\d{2})(\.\d+)?',  # hh:mm:ss[.sss...]
        r'(\d{2}):(\d{2})(\.\d+)?',          # hh:mm[.sss...]
        r'(\d{2})(:\d{2})?(\.\d+)?',         # hh[:mm][.sss...]
    ]
    
    tz_patterns = [
        r'Z',                             # UTC
        r'([+-]\d{2}):?(\d{2})?',         # ±HH:MM
        r'([+-]\d{2})(\d{2})?',            # ±HHMM
        r'([+-]\d{2})'                     # ±HH
    ]
    
    # Combine patterns
    date_regex = re.compile(r'|'.join(date_patterns))
    time_regex = re.compile(r'|'.join(time_patterns))
    tz_regex = re.compile(r'|'.join(tz_patterns))

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
        year, month, day = map(int, date_match.groups()[0:3])
    elif date_match.group(4):  # YYYY-Www
        year, week = map(int, date_match.groups()[3:5])
        day = 1  # Default to first day of the week
    elif date_match.group(6):  # YYYY-Www-D
        year, week, week_day = map(int, date_match.groups()[6:9])
        day = week_day

    # Handle week-based dates
    if week is not None:
        first_day_of_year = datetime(year, 1, 1)
        first_weekday = first_day_of_year.isoweekday()
        days_to_first_week = (7 - first_weekday) % 7
        first_week_start = first_day_of_year + timedelta(days=days_to_first_week)
        date = first_week_start + timedelta(weeks=week - 1, days=day - 1)
    else:
        date = datetime(year, month or 1, day or 1)

    # Parse time
    time_match = time_regex.fullmatch(time_str)
    if time_match:
        hour, minute, second = map(int, time_match.groups()[0:3])
        if time_match.group(4):  # Handle fractional seconds
            microsecond = int(float(time_match.group(4)) * 1_000_000)
        else:
            microsecond = 0
    else:
        hour, minute, second, microsecond = 0, 0, 0, 0

    # Handle special case for midnight
    if hour == 24:
        hour, minute, second = 0, 0, 0

    # Combine date and time
    dt = datetime.combine(date, datetime.time(hour, minute, second, microsecond))

    # Parse timezone
    tz_match = tz_regex.search(dt_str)
    if tz_match:
        tz_str = tz_match.group(0)
        if tz_str == 'Z':
            dt = dt.replace(tzinfo=tz.tzutc())
        else:
            sign = 1 if tz_str[0] == '+' else -1
            if ':' in tz_str:
                hours, minutes = map(int, tz_str[1:].split(':'))
            else:
                hours = int(tz_str[1:])
                minutes = 0
            offset = timedelta(hours=sign * hours, minutes=sign * minutes)
            dt = dt.replace(tzinfo=tz.tzoffset(None, offset.total_seconds()))

    return dt