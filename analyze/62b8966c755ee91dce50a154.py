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
        r'(?P<year>\d{4})-(?P<week>\d{2})-?(?P<day>\d)?',  # YYYY-Www or YYYY-Www-D
        r'(?P<year>\d{4})-(?P<month>\d{2})',                # YYYY-MM
        r'(?P<year>\d{4})',                                 # YYYY
    ]

    time_patterns = [
        r'(?P<hour>\d{1,2}):(?P<minute>\d{2}):?(?P<second>\d{2})?\.?(?P<microsecond>\d{1,6})?',  # hh:mm:ss.ssssss
        r'(?P<hour>\d{1,2}):(?P<minute>\d{2})',  # hh:mm
        r'(?P<hour>\d{1,2})',                     # hh
    ]

    tz_patterns = [
        r'Z',  # UTC
        r'(?P<sign>[+-])(?P<hour>\d{2}):?(?P<minute>\d{2})?',  # ±HH:MM
        r'(?P<sign>[+-])(?P<hour>\d{2})(?P<minute>\d{2})?',    # ±HHMM
        r'(?P<sign>[+-])(?P<hour>\d{2})',                        # ±HH
    ]

    # Combine patterns
    full_pattern = r'^(?P<date>' + '|'.join(date_patterns) + r')' + \
                   r'(T(?P<time>' + '|'.join(time_patterns) + r'))?' + \
                   r'(?P<tz>' + '|'.join(tz_patterns) + r')?$'

    match = re.match(full_pattern, dt_str)
    if not match:
        raise ValueError("Invalid ISO-8601 date string")

    # Extract date components
    date_components = match.groupdict()
    year = int(date_components['year'])
    month = int(date_components.get('month', 1))
    day = int(date_components.get('day', 1))

    # Handle week-based dates
    if date_components.get('week'):
        week = int(date_components['week'])
        day = int(date_components.get('day', 1)) or 1
        # Calculate the first day of the year
        first_day_of_year = datetime(year, 1, 1)
        # Calculate the first Monday of the year
        first_monday = first_day_of_year + timedelta(days=(7 - first_day_of_year.isoweekday()) % 7)
        # Calculate the date
        date = first_monday + timedelta(weeks=week - 1, days=day - 1)
    else:
        date = datetime(year, month, day)

    # Extract time components
    if date_components.get('time'):
        time_components = date_components['time'].split(':')
        hour = int(time_components[0])
        minute = int(time_components[1]) if len(time_components) > 1 else 0
        second = int(time_components[2]) if len(time_components) > 2 else 0
        microsecond = int(time_components[3]) if len(time_components) > 3 else 0
        time = date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
    else:
        time = date

    # Handle timezone
    tz_info = None
    if date_components.get('tz'):
        tz_str = date_components['tz']
        if tz_str == 'Z':
            tz_info = tz.tzutc()
        else:
            sign = 1 if tz_str[0] == '+' else -1
            hour = int(tz_str[1:3])
            minute = int(tz_str[3:5]) if len(tz_str) > 3 else 0
            tz_info = tz.tzoffset(None, sign * (hour * 3600 + minute * 60))

    # Return the final datetime object
    return time.replace(tzinfo=tz_info)