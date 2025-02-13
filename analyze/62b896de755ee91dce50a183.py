def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    from dateutil import parser
    from datetime import datetime

    if not isinstance(timestr, str):
        raise TypeError("Input must be a string")

    if default is not None and not isinstance(default, datetime):
        raise TypeError("Default must be a datetime object or None")

    try:
        dt = parser.parse(timestr, default=default, ignoretz=ignoretz, tzinfos=tzinfos, **kwargs)
    except (ValueError, OverflowError) as e:
        raise ParserError(f"Error parsing date string: {e}")

    return dt