def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """
    Parse the date/time string into a :class:`datetime.datetime` object.
    
    :param timestr: Any date/time string using the supported formats.
    :param default: The default datetime object, if this is a datetime object and not ``None``, 
                   elements specified in ``timestr`` replace elements in the default object.
    :param ignoretz: If set ``True``, time zones in parsed strings are ignored and a naive 
                    :class:`datetime.datetime` object is returned.
    :param tzinfos: Additional time zone names / aliases which may be present in the string.
    :param **kwargs: Keyword arguments as passed to ``_parse()``.
    :return: Returns a :class:`datetime.datetime` object or tuple with datetime and fuzzy tokens
    :raises: ParserError, TypeError, OverflowError
    """
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not "
                      f"{type(timestr).__name__}")

    # Handle empty string
    if not timestr:
        raise ParserError("String is empty")

    try:
        # Parse the string using internal _parse method
        res, tokens = self._parse(timestr, **kwargs)

        # If no tokens found and fuzzy parsing not enabled, raise error
        if not tokens and not kwargs.get('fuzzy', False):
            raise ParserError("String does not contain a date.")

        # Build datetime object
        if res.year is None:
            res.year = default.year if default else datetime.now().year
        if res.month is None:
            res.month = default.month if default else 1
        if res.day is None:
            res.day = default.day if default else 1

        # Create aware or naive datetime based on ignoretz
        if res.tzname and not ignoretz:
            if tzinfos is not None:
                # Handle tzinfos dictionary or callable
                if isinstance(tzinfos, dict):
                    tz = tzinfos.get(res.tzname)
                else:
                    tz = tzinfos(res.tzname, res.tzoffset)
                if tz is None:
                    raise ParserError(f"Unknown timezone name: {res.tzname}")
            elif res.tzoffset:
                tz = datetime.timezone(datetime.timedelta(seconds=res.tzoffset))
            else:
                tz = None
        else:
            tz = None

        dt = datetime.datetime(
            res.year, res.month, res.day,
            res.hour if res.hour is not None else 0,
            res.minute if res.minute is not None else 0,
            res.second if res.second is not None else 0,
            res.microsecond if res.microsecond is not None else 0,
            tzinfo=tz
        )

        if kwargs.get('fuzzy_with_tokens', False):
            return dt, tokens
        else:
            return dt

    except (ValueError, OverflowError) as e:
        raise ParserError(str(e))