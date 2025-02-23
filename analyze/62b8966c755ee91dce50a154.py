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
    offset_pattern = r'([+-]\d{2}):?(\d{2})?|Z'

    # Combine patterns
    iso_pattern = re.compile(
        f'^{date_pattern}(?:-W{week_pattern})?(?:{time_pattern})?({offset_pattern})?$'
    )

    match = iso_pattern.match(dt_str)
    if not match:
        raise ValueError(f"Invalid ISO-8601 string: {dt_str}")

    # Extract date components
    year, month, day = match.group(1), match.group(2), match.group(3)
    week, week_day = match.group(5), match.group(6)
    hour, minute, second, microsecond = match.group(8), match.group(9), match.group(10), match.group(11)
    offset = match.group(12)

    # Handle date parsing
    if week:
        # ISO week date
        year, week = int(year), int(week)
        if week_day:
            week_day = int(week_day)
        else:
            week_day = 0  # Default to Monday
        date = datetime.fromisocalendar(year, week, week_day)
    else:
        # Regular date
        year = int(year)
        month = int(month) if month else 1
        day = int(day) if day else 1
        date = datetime(year, month, day)

    # Handle time parsing
    if hour:
        hour = int(hour)
        minute = int(minute) if minute else 0
        second = int(second) if second else 0
        microsecond = int(microsecond.ljust(6, '0')) if microsecond else 0
        date = date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

    # Handle timezone offset
    if offset == 'Z':
        tzinfo = tz.tzutc()
    elif offset:
        sign = 1 if offset[0] == '+' else -1
        hours = int(offset[1:3])
        minutes = int(offset[3:5]) if len(offset) > 3 else 0
        total_offset = sign * (hours * 3600 + minutes * 60)
        tzinfo = tz.tzoffset(None, total_offset)
    else:
        tzinfo = None

    return date.replace(tzinfo=tzinfo)