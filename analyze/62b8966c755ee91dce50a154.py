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
    date_pattern = r'(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?'
    week_pattern = r'(\d{4})-W(\d{2})(?:-?(\d{1}))?'
    time_pattern = r'T(\d{1,2})(?::(\d{2})(?::(\d{2})(?:\.(\d{1,6}))?)?)?'
    tz_pattern = r'([+-]\d{2}:\d{2}|Z|[+-]\d{4}|[+-]\d{2})?'

    # Combine patterns
    full_pattern = rf'^{date_pattern}(?:-W{week_pattern})?({time_pattern})?({tz_pattern})?$'
    match = re.match(full_pattern, dt_str)

    if not match:
        raise ValueError(f"Invalid ISO-8601 string: {dt_str}")

    # Extract date components
    year, month, day = match.group(1), match.group(2), match.group(3)
    if month is None:
        month = 1
    if day is None:
        day = 1

    # Handle week date if present
    week_year, week, week_day = match.group(4), match.group(5), match.group(6)
    if week_year and week:
        week_year = int(week_year)
        week = int(week)
        week_day = int(week_day) if week_day else 1
        date = datetime.strptime(f'{week_year}-W{week}-{week_day}', "%Y-W%W-%w")
    else:
        date = datetime(int(year), int(month), int(day))

    # Extract time components
    hour, minute, second, microsecond = match.group(7), match.group(8), match.group(9), match.group(10)
    if hour is None:
        hour = 0
    if minute is None:
        minute = 0
    if second is None:
        second = 0
    if microsecond is None:
        microsecond = 0
    else:
        microsecond = int(microsecond.ljust(6, '0'))  # Pad to 6 digits

    # Create datetime object
    date = date.replace(hour=int(hour), minute=int(minute), second=int(second), microsecond=microsecond)

    # Handle timezone
    tz_offset = match.group(11)
    if tz_offset == 'Z':
        date = date.replace(tzinfo=tz.tzutc())
    elif tz_offset:
        sign = 1 if tz_offset[0] == '+' else -1
        if ':' in tz_offset:
            hours, minutes = map(int, tz_offset[1:].split(':'))
        else:
            hours = int(tz_offset[1:3])
            minutes = 0
        offset = timedelta(hours=sign * hours, minutes=sign * minutes)
        date = date.replace(tzinfo=tz.tzoffset(None, offset.total_seconds()))

    return date