def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    from dateutil import parser
    from datetime import datetime

    if not isinstance(timestr, str):
        raise TypeError("timestr must be a string")

    if default is not None and not isinstance(default, datetime):
        raise TypeError("default must be a datetime object or None")

    if ignoretz:
        return parser.parse(timestr, default=default, tzinfos=tzinfos, **kwargs).replace(tzinfo=None)

    return parser.parse(timestr, default=default, tzinfos=tzinfos, **kwargs)