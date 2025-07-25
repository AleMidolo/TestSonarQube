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

        # If no tokens were found, raise error
        if res is None:
            raise ParserError("String does not contain a date.")

        # Build datetime object
        if default is None:
            default = datetime.datetime.now().replace(
                hour=0, minute=0, second=0, microsecond=0)

        # Replace any elements specified in res
        repl = {}
        for attr in ["year", "month", "day", "hour", 
                    "minute", "second", "microsecond"]:
            if getattr(res, attr) is not None:
                repl[attr] = getattr(res, attr)

        dt = default.replace(**repl)

        # Handle timezone
        if res.tzname is not None and not ignoretz:
            if tzinfos is None:
                raise ParserError("tzinfos parameter required for %s" % res.tzname)
                
            if callable(tzinfos):
                tz = tzinfos(res.tzname, res.tzoffset)
            else:
                tz = tzinfos.get(res.tzname)
                
            if tz is None:
                raise ParserError("Unknown timezone name: %s" % res.tzname)
                
            dt = dt.replace(tzinfo=tz)

        if kwargs.get('fuzzy_with_tokens', False):
            return dt, tokens
        else:
            return dt

    except (TypeError, ValueError, OverflowError) as e:
        raise ParserError(str(e))