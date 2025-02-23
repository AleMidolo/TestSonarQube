def isoparse(self, dt_str):
    """
    Parse an ISO-8601 datetime string into a :class:`datetime.datetime`.

    An ISO-8601 datetime string consists of a date portion, followed
    optionally by a time portion - the date and time portions are separated
    by a single character separator, which is ``T`` in the official
    standard. Incomplete date formats (such as ``YYYY-MM``) may *not* be
    combined with a time portion.

    Supported date formats are:

    Common:

    - ``YYYY``
    - ``YYYY-MM`` or ``YYYYMM``
    - ``YYYY-MM-DD`` or ``YYYYMMDD``

    Uncommon:

    - ``YYYY-Www`` or ``YYYYWww`` - ISO week (day defaults to 0)
    - ``YYYY-Www-D`` or ``YYYYWwwD`` - ISO week and day

    The ISO week and day numbering follows the same logic as
    :func:`datetime.date.isocalendar`.

    Supported time formats are:

    - ``hh``
    - ``hh:mm`` or ``hhmm``
    - ``hh:mm:ss`` or ``hhmmss``
    - ``hh:mm:ss.ssssss`` (Up to 6 sub-second digits)

    Midnight is a special case for `hh`, as the standard supports both
    00:00 and 24:00 as a representation. The decimal separator can be
    either a dot or a comma.


    .. caution::

        Support for fractional components other than seconds is part of the
        ISO-8601 standard, but is not currently implemented in this parser.

    Supported time zone offset formats are:

    - `Z` (UTC)
    - `±HH:MM`
    - `±HHMM`
    - `±HH`

    Offsets will be represented as :class:`dateutil.tz.tzoffset` objects,
    with the exception of UTC, which will be represented as
    :class:`dateutil.tz.tzutc`. Time zone offsets equivalent to UTC (such
    as `+00:00`) will also be represented as :class:`dateutil.tz.tzutc`.

    :param dt_str:
        A string or stream containing only an ISO-8601 datetime string

    :return:
        Returns a :class:`datetime.datetime` representing the string.
        Unspecified components default to their lowest value.

    .. warning::

        As of version 2.7.0, the strictness of the parser should not be
        considered a stable part of the contract. Any valid ISO-8601 string
        that parses correctly with the default settings will continue to
        parse correctly in future versions, but invalid strings that
        currently fail (e.g. ``2017-01-01T00:00+00:00:00``) are not
        guaranteed to continue failing in future versions if they encode
        a valid date.

    .. versionadded:: 2.7.0
    """
    from datetime import datetime, timedelta
    import re
    from dateutil import tz

    # Define regex patterns for parsing
    date_patterns = [
        r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',  # YYYY-MM-DD
        r'(?P<year>\d{4})-(?P<week>\d{2})',  # YYYY-Www
        r'(?P<year>\d{4})W(?P<week>\d{2})',  # YYYYWww
        r'(?P<year>\d{4})',  # YYYY
    ]

    time_patterns = [
        r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})(\.(?P<subsecond>\d+))?',  # hh:mm:ss
        r'(?P<hour>\d{2}):(?P<minute>\d{2})',  # hh:mm
        r'(?P<hour>\d{2})',  # hh
    ]

    tz_patterns = [
        r'Z',  # UTC
        r'(?P<sign>[+-])(?P<hour>\d{2}):(?P<minute>\d{2})',  # ±HH:MM
        r'(?P<sign>[+-])(?P<hour>\d{2})(?P<minute>\d{2})',  # ±HHMM
        r'(?P<sign>[+-])(?P<hour>\d{2})',  # ±HH
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

    year = int(date_match.group('year'))
    month = int(date_match.group('month') or 1)
    day = int(date_match.group('day') or 1)

    # Handle ISO week date
    if date_match.group('week'):
        week = int(date_match.group('week'))
        # Calculate the first day of the year
        first_day_of_year = datetime(year, 1, 1)
        # Calculate the first Monday of the year
        first_monday = first_day_of_year + timedelta(days=(7 - first_day_of_year.isoweekday()) % 7)
        # Calculate the date from the week number
        date = first_monday + timedelta(weeks=week - 1)
        day = date.isoweekday()  # Default to Monday

    # Parse time
    time_match = time_regex.fullmatch(time_str)
    if time_match:
        hour = int(time_match.group('hour') or 0)
        minute = int(time_match.group('minute') or 0)
        second = int(time_match.group('second') or 0)
        subsecond = int(time_match.group('subsecond') or 0) if time_match.group('subsecond') else 0
    else:
        hour, minute, second, subsecond = 0, 0, 0, 0

    # Handle midnight case
    if hour == 24:
        hour = 0
        day += 1

    # Parse timezone
    tzinfo = None
    tz_match = tz_regex.fullmatch(time_str.split('T')[-1]) if 'T' in dt_str else None
    if tz_match:
        if tz_match.group('sign') == 'Z':
            tzinfo = tz.tzutc()
        else:
            sign = 1 if tz_match.group('sign') == '+' else -1
            tz_hour = int(tz_match.group('hour'))
            tz_minute = int(tz_match.group('minute') or 0)
            tzinfo = tz.tzoffset(None, sign * (tz_hour * 3600 + tz_minute * 60))

    # Create datetime object
    dt = datetime(year, month, day, hour, minute, second, subsecond, tzinfo=tzinfo)

    return dt