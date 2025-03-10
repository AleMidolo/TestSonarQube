from datetime import datetime
from dateutil.parser import parse as dateutil_parse
from dateutil.tz import gettz
from dateutil.parser import ParserError

def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """
    Parse the date/time string into a :class:`datetime.datetime` object.

    :param timestr:
        Any date/time string using the supported formats.

    :param default:
        The default datetime object, if this is a datetime object and not
        ``None``, elements specified in ``timestr`` replace elements in the
        default object.

    :param ignoretz:
        If set ``True``, time zones in parsed strings are ignored and a
        naive :class:`datetime.datetime` object is returned.

    :param tzinfos:
        Additional time zone names / aliases which may be present in the
        string. This argument maps time zone names (and optionally offsets
        from those time zones) to time zones. This parameter can be a
        dictionary with timezone aliases mapping time zone names to time
        zones or a function taking two parameters (``tzname`` and
        ``tzoffset``) and returning a time zone.

        The timezones to which the names are mapped can be an integer
        offset from UTC in seconds or a :class:`tzinfo` object.

    :param \*\*kwargs:
        Keyword arguments as passed to ``_parse()``.

    :return:
        Returns a :class:`datetime.datetime` object or, if the
        ``fuzzy_with_tokens`` option is ``True``, returns a tuple, the
        first element being a :class:`datetime.datetime` object, the second
        a tuple containing the fuzzy tokens.

    :raises ParserError:
        Raised for invalid or unknown string format, if the provided
        :class:`tzinfo` is not in a valid format, or if an invalid date
        would be created.

    :raises TypeError:
        Raised for non-string or character stream input.

    :raises OverflowError:
        Raised if the parsed date exceeds the largest valid C integer on
        your system.
    """
    try:
        if not isinstance(timestr, str):
            raise TypeError("Input must be a string or character stream.")

        if default is not None and not isinstance(default, datetime):
            raise TypeError("Default must be a datetime object or None.")

        if ignoretz:
            tzinfos = None

        parsed_datetime = dateutil_parse(timestr, default=default, ignoretz=ignoretz, tzinfos=tzinfos, **kwargs)

        return parsed_datetime

    except ParserError as e:
        raise ParserError(f"Invalid or unknown string format: {e}")
    except OverflowError as e:
        raise OverflowError(f"Parsed date exceeds the largest valid C integer: {e}")