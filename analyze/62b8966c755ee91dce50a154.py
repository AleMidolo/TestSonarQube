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
    from datetime import datetime
    import re
    from dateutil import tz

    # Define regex patterns for parsing
    date_pattern = r'(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?'
    week_pattern = r'(\d{4})-W(\d{2})(?:-?(\d{1}))?'
    time_pattern = r'T(\d{1,2})(?::(\d{2})(?::(\d{2})(?:\.(\d{1,6}))?)?)?'
    tz_pattern = r'([+-]\d{2}:\d{2}|Z|[+-]\d{4}|[+-]\d{2})?'

    # Combine patterns
    full_pattern = rf'^{date_pattern}(?:-W{week_pattern})?({time_pattern})?({tz_pattern})?$'
    match = re.match(full_pattern, dt_str)

    if not match:
        raise ValueError("Invalid ISO-8601 datetime string")

    # Extract date components
    year, month, day = match.group(1), match.group(2), match.group(3)
    if month is None:
        month = 1
    if day is None:
        day = 1

    # Extract time components
    hour, minute, second, microsecond = match.group(4), match.group(5), match.group(6), match.group(7)
    if hour is None:
        hour = 0
    if minute is None:
        minute = 0
    if second is None:
        second = 0
    if microsecond is None:
        microsecond = 0

    # Handle time zone
    tzinfo = None
    tz_str = match.group(8)
    if tz_str == 'Z':
        tzinfo = tz.tzutc()
    elif tz_str:
        if len(tz_str) == 5:  # ±HH:MM
            sign = 1 if tz_str[0] == '+' else -1
            hours, minutes = map(int, tz_str[1:].split(':'))
            tzinfo = tz.tzoffset(None, sign * (hours * 3600 + minutes * 60))
        elif len(tz_str) == 3:  # ±HH
            sign = 1 if tz_str[0] == '+' else -1
            hours = int(tz_str[1:])
            tzinfo = tz.tzoffset(None, sign * hours * 3600)
        else:  # ±HHMM
            sign = 1 if tz_str[0] == '+' else -1
            hours = int(tz_str[1:3])
            minutes = int(tz_str[3:5])
            tzinfo = tz.tzoffset(None, sign * (hours * 3600 + minutes * 60))

    # Create datetime object
    return datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond), tzinfo)