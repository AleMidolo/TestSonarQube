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
    date_pattern = r'(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?'
    week_pattern = r'(\d{4})-W(\d{2})(?:-?(\d{1}))?'
    time_pattern = r'(\d{2})(?::(\d{2})(?::(\d{2})(?:\.(\d{1,6}))?)?)?'
    tz_pattern = r'Z|([+-]\d{2}):?(\d{2})?|([+-]\d{2})(\d{2})?|([+-]\d{2})'

    # Combine patterns
    iso_pattern = re.compile(
        rf'^{date_pattern}(?:T{time_pattern})?(?:{tz_pattern})?$'
    )

    match = iso_pattern.match(dt_str)
    if not match:
        raise ValueError(f"Invalid ISO-8601 date string: {dt_str}")

    # Extract date components
    year = int(match.group(1))
    month = int(match.group(2) or 1)
    day = int(match.group(3) or 1)

    # Handle week-based dates
    if match.group(2) is None and match.group(3) is None:
        week = int(match.group(4) or 1)
        day_of_week = int(match.group(5) or 0)
        date = datetime.fromisocalendar(year, week, day_of_week)
    else:
        date = datetime(year, month, day)

    # Extract time components
    hour = int(match.group(6) or 0)
    minute = int(match.group(7) or 0)
    second = int(match.group(8) or 0)
    microsecond = int(match.group(9) or 0)

    # Set time
    date = date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

    # Handle timezone
    tzinfo = None
    if match.group(10):
        if match.group(10) == 'Z':
            tzinfo = tz.tzutc()
        else:
            sign = match.group(11)
            if match.group(12):
                tzinfo = tz.tzoffset(None, int(sign + match.group(11)) * 3600 + int(match.group(12)) * 60)
            else:
                tzinfo = tz.tzoffset(None, int(sign + match.group(13)) * 3600)

    if tzinfo:
        date = date.replace(tzinfo=tzinfo)

    return date