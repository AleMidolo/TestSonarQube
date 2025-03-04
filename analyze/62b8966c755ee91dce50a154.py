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
        r'(?P<year>\d{4})-(?P<week>\d{2})-W(?P<day>\d)',   # YYYY-Www-D
        r'(?P<year>\d{4})-(?P<week>\d{2})',                 # YYYY-Www
        r'(?P<year>\d{4})',                                 # YYYY
        r'(?P<year>\d{4})(?P<month>\d{2})',                 # YYYYMM
        r'(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})',   # YYYYMMDD
    ]

    time_patterns = [
        r'(?P<hour>\d{1,2}):(?P<minute>\d{2}):(?P<second>\d{2})(\.(?P<microsecond>\d{1,6}))?',  # hh:mm:ss.ssssss
        r'(?P<hour>\d{1,2}):(?P<minute>\d{2})(\.(?P<microsecond>\d{1,6}))?',                      # hh:mm.ssssss
        r'(?P<hour>\d{1,2})(:(?P<minute>\d{2}))?(\.(?P<microsecond>\d{1,6}))?',                   # hh or hh:mm
    ]

    tz_patterns = [
        r'Z',  # UTC
        r'(?P<sign>[+-])(?P<hour>\d{2}):?(?P<minute>\d{2})?',  # ±HH:MM
        r'(?P<sign>[+-])(?P<hour>\d{2})(?P<minute>\d{2})?',     # ±HHMM
        r'(?P<sign>[+-])(?P<hour>\d{2})',                       # ±HH
    ]

    # Combine patterns
    full_pattern = r'^\s*(' + '|'.join(date_patterns) + r')' + r'([T ](' + '|'.join(time_patterns) + r'))?(' + '|'.join(tz_patterns) + r')?\s*$'
    match = re.match(full_pattern, dt_str)

    if not match:
        raise ValueError("Invalid ISO-8601 format")

    # Extract date components
    year = int(match.group('year'))
    month = int(match.group('month') or 1)
    day = int(match.group('day') or 1)
    week = match.group('week')
    weekday = int(match.group('day')) if week else 0

    if week:
        # Calculate date from ISO week date
        first_day_of_year = datetime(year, 1, 1)
        first_weekday = first_day_of_year.isocalendar()[2]
        days_to_first_week = (7 - first_weekday) % 7
        first_week_start = first_day_of_year + timedelta(days=days_to_first_week)
        date = first_week_start + timedelta(weeks=int(week) - 1, days=weekday)
    else:
        date = datetime(year, month, day)

    # Extract time components
    hour = int(match.group('hour') or 0)
    minute = int(match.group('minute') or 0)
    second = int(match.group('second') or 0)
    microsecond = int(match.group('microsecond') or 0)

    # Handle special case for midnight
    if hour == 24 and minute == 0 and second == 0:
        date = date.replace(day=date.day + 1, hour=0, minute=0, second=0, microsecond=0)

    # Create datetime object
    dt = date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

    # Handle timezone
    tz_offset = match.group(5)
    if tz_offset == 'Z':
        dt = dt.replace(tzinfo=tz.tzutc())
    elif tz_offset:
        sign = 1 if match.group('sign') == '+' else -1
        tz_hour = int(match.group('hour'))
        tz_minute = int(match.group('minute') or 0)
        offset = sign * (tz_hour * 3600 + tz_minute * 60)
        dt = dt.replace(tzinfo=tz.tzoffset(None, offset))

    return dt