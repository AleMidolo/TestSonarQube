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
    iso_pattern = re.compile(f'^{date_pattern}(?:-W{week_pattern})?({time_pattern})?({tz_pattern})?$')

    match = iso_pattern.match(dt_str)
    if not match:
        raise ValueError(f"Invalid ISO-8601 string: {dt_str}")

    # Extract date components
    year, month, day = match.group(1), match.group(2), match.group(3)
    week, week_day = match.group(5), match.group(6)
    hour, minute, second, microsecond = match.group(7), match.group(8), match.group(9), match.group(10)
    tz_info = match.group(11)

    # Handle date
    if week:
        year, week = int(year), int(week)
        if week_day:
            week_day = int(week_day)
            dt = datetime.fromisocalendar(year, week, week_day)
        else:
            dt = datetime.fromisocalendar(year, week, 1)
    else:
        year = int(year)
        month = int(month) if month else 1
        day = int(day) if day else 1
        dt = datetime(year, month, day)

    # Handle time
    if hour:
        hour = int(hour)
        minute = int(minute) if minute else 0
        second = int(second) if second else 0
        microsecond = int(microsecond.ljust(6, '0')) if microsecond else 0
        dt = dt.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

    # Handle timezone
    if tz_info == 'Z':
        dt = dt.replace(tzinfo=tz.tzutc())
    elif tz_info:
        sign = 1 if tz_info[0] == '+' else -1
        if len(tz_info) == 5:  # ±HH:MM
            hours, minutes = map(int, tz_info[1:].split(':'))
            offset = timedelta(hours=hours * sign, minutes=minutes * sign)
        elif len(tz_info) == 3:  # ±HH
            hours = int(tz_info[1:])
            offset = timedelta(hours=hours * sign)
        else:  # ±HHMM
            hours = int(tz_info[1:3])
            minutes = int(tz_info[3:5])
            offset = timedelta(hours=hours * sign, minutes=minutes * sign)
        dt = dt.replace(tzinfo=tz.tzoffset(None, offset.total_seconds()))

    return dt