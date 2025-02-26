def isoparse(self, dt_str):
    """
    Analizza una stringa datetime in formato ISO-8601 in un oggetto :class:`datetime.datetime`.

    Una stringa datetime in formato ISO-8601 consiste in una parte relativa alla data, seguita
    opzionalmente da una parte relativa all'ora. Le due parti sono separate da un singolo carattere
    separatore, che è ``T`` nello standard ufficiale. I formati di data incompleti (come ``YYYY-MM``)
    *non* possono essere combinati con una parte relativa all'ora.

    I formati di data supportati sono:

    Comuni:

    - ``YYYY``
    - ``YYYY-MM`` o ``YYYYMM``
    - ``YYYY-MM-DD`` o ``YYYYMMDD``

    Non comuni:

    - ``YYYY-Www`` o ``YYYYWww`` - Settimana ISO (il giorno predefinito è 0)
    - ``YYYY-Www-D`` o ``YYYYWwwD`` - Settimana ISO e giorno

    La numerazione delle settimane e dei giorni ISO segue la stessa logica di
    :func:`datetime.date.isocalendar`.

    I formati di ora supportati sono:

    - ``hh``
    - ``hh:mm`` o ``hhmm``
    - ``hh:mm:ss`` o ``hhmmss``
    - ``hh:mm:ss.ssssss`` (fino a 6 cifre per i sotto-secondi)

    La mezzanotte è un caso speciale per `hh`, poiché lo standard supporta sia
    00:00 che 24:00 come rappresentazione. Il separatore decimale può essere
    sia un punto che una virgola.

    .. attenzione::

        Il supporto per componenti frazionari diversi dai secondi fa parte dello
        standard ISO-8601, ma non è attualmente implementato in questo parser.

    I formati di offset del fuso orario supportati sono:

    - `Z` (UTC)
    - `±HH:MM`
    - `±HHMM`
    - `±HH`

    Gli offset saranno rappresentati come oggetti :class:`dateutil.tz.tzoffset`,
    con l'eccezione di UTC, che sarà rappresentato come :class:`dateutil.tz.tzutc`.
    Gli offset del fuso orario equivalenti a UTC (come `+00:00`) saranno anch'essi
    rappresentati come :class:`dateutil.tz.tzutc`.

    :param dt_str:
        Una stringa o un flusso contenente solo una stringa datetime in formato ISO-8601.

    :return:
        Restituisce un oggetto :class:`datetime.datetime` che rappresenta la stringa.
        I componenti non specificati assumono il loro valore minimo.

    .. avvertenza::

        A partire dalla versione 2.7.0, la rigidità del parser non deve essere considerata
        una parte stabile del contratto. Qualsiasi stringa ISO-8601 valida che viene analizzata
        correttamente con le impostazioni predefinite continuerà a essere analizzata correttamente
        nelle versioni future, ma le stringhe non valide che attualmente falliscono (ad esempio
        ``2017-01-01T00:00+00:00:00``) non sono garantite di continuare a fallire nelle versioni
        future se codificano una data valida.

    .. versioneaggiunta:: 2.7.0
    """
    from datetime import datetime, timedelta
    import re
    from dateutil import tz

    # Regex patterns for parsing
    date_patterns = [
        r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',  # YYYY-MM-DD
        r'(?P<year>\d{4})-(?P<week>\d{2})-W(?P<weekday>\d)',  # YYYY-Www-D
        r'(?P<year>\d{4})-(?P<week>\d{2})',  # YYYY-Www
        r'(?P<year>\d{4})',  # YYYY
        r'(?P<year>\d{4})(?P<month>\d{2})',  # YYYYMM
        r'(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})',  # YYYYMMDD
    ]

    time_patterns = [
        r'(?P<hour>\d{1,2}):(?P<minute>\d{2})(?::(?P<second>\d{2})(\.(?P<subsecond>\d{1,6}))?)?',  # hh:mm:ss.ssssss
        r'(?P<hour>\d{1,2})(?P<minute>\d{2})(?::(?P<second>\d{2})(\.(?P<subsecond>\d{1,6}))?)?',  # hhmmss.ssssss
        r'(?P<hour>\d{1,2})(?::(?P<minute>\d{2}))?',  # hh:mm
        r'(?P<hour>\d{1,2})(?P<minute>\d{2})?',  # hhmm
    ]

    tz_patterns = [
        r'Z',  # UTC
        r'(?P<sign>[+-])(?P<hour>\d{2}):(?P<minute>\d{2})',  # ±HH:MM
        r'(?P<sign>[+-])(?P<hour>\d{2})(?P<minute>\d{2})',  # ±HHMM
        r'(?P<sign>[+-])(?P<hour>\d{2})',  # ±HH
    ]

    # Split date and time
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T', 1)
    else:
        date_str, time_str = dt_str, ''

    # Parse date
    date_match = None
    for pattern in date_patterns:
        date_match = re.fullmatch(pattern, date_str)
        if date_match:
            break

    if not date_match:
        raise ValueError("Invalid date format")

    year = int(date_match.group('year'))
    month = int(date_match.group('month') or 1)
    day = int(date_match.group('day') or 1)

    if date_match.group('week'):
        week = int(date_match.group('week'))
        weekday = int(date_match.group('weekday') or 0)
        # Calculate the date from ISO week date
        first_day_of_year = datetime(year, 1, 1)
        first_weekday = first_day_of_year.isocalendar()[2]
        days_to_first_week = (7 - first_weekday) % 7
        first_week_start = first_day_of_year + timedelta(days=days_to_first_week)
        date = first_week_start + timedelta(weeks=week - 1, days=weekday)
    else:
        date = datetime(year, month, day)

    # Parse time
    time_match = None
    for pattern in time_patterns:
        time_match = re.fullmatch(pattern, time_str)
        if time_match:
            break

    hour = int(time_match.group('hour') or 0)
    minute = int(time_match.group('minute') or 0)
    second = int(time_match.group('second') or 0)
    subsecond = int(time_match.group('subsecond') or 0)

    # Handle midnight case
    if hour == 24:
        hour = 0
        date += timedelta(days=1)

    time = timedelta(hours=hour, minutes=minute, seconds=second, microseconds=subsecond * 1000)

    # Combine date and time
    dt = datetime.combine(date.date(), datetime.min.time()) + time

    # Parse timezone
    tzinfo = None
    if time_str:
        for pattern in tz_patterns:
            tz_match = re.search(pattern, time_str)
            if tz_match:
                sign = tz_match.group('sign')
                if sign:
                    offset_hour = int(tz_match.group('hour'))
                    offset_minute = int(tz_match.group('minute') or 0)
                    total_offset = offset_hour * 3600 + offset_minute * 60
                    if sign == '-':
                        total_offset = -total_offset
                    tzinfo = tz.tzoffset(None, total_offset)
                else:
                    tzinfo = tz.tzutc()
                break

    if tzinfo:
        dt = dt.replace(tzinfo=tzinfo)

    return dt