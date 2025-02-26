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
    date_pattern = r'(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?(?:W(\d{2})(?:-?(\d))?)?'
    time_pattern = r'T(\d{1,2})(?::(\d{2})(?::(\d{2})(?:\.(\d{1,6}))?)?)?'
    tz_pattern = r'([+-]\d{2}:\d{2}|Z|[+-]\d{2}\d{2}|[+-]\d{2})?'

    # Combine patterns
    full_pattern = re.compile(f'^{date_pattern}(?:{time_pattern})?{tz_pattern}?$')

    match = full_pattern.match(dt_str)
    if not match:
        raise ValueError(f"Invalid ISO-8601 datetime string: {dt_str}")

    # Extract date components
    year = int(match.group(1))
    month = int(match.group(2) or 1)
    day = int(match.group(3) or 1)
    week = match.group(4)
    week_day = match.group(5)

    if week:
        # ISO week date
        week = int(week)
        week_day = int(week_day or 1)
        # Calculate the first day of the year
        first_day_of_year = datetime(year, 1, 1)
        # Calculate the first Monday of the year
        first_monday = first_day_of_year + timedelta(days=(7 - first_day_of_year.isoweekday()) % 7)
        # Calculate the date
        date = first_monday + timedelta(weeks=week - 1, days=week_day - 1)
    else:
        # Regular date
        date = datetime(year, month, day)

    # Extract time components
    hour = int(match.group(6) or 0)
    minute = int(match.group(7) or 0)
    second = int(match.group(8) or 0)
    microsecond = int(match.group(9) or 0)

    # Create datetime object
    dt = date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

    # Extract timezone
    tz_str = match.group(10)
    if tz_str == 'Z':
        dt = dt.replace(tzinfo=tz.tzutc())
    elif tz_str:
        if ':' in tz_str:
            offset = tz.tzoffset(None, int(tz_str[:3]) * 3600 + int(tz_str[4:]) * 60)
        else:
            offset = tz.tzoffset(None, int(tz_str) * 3600)
        dt = dt.replace(tzinfo=offset)

    return dt