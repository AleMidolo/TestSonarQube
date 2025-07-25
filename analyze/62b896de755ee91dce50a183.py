def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """
    Parse a datetime string into a datetime.datetime object.
    
    Args:
        timestr: Any datetime string using supported formats
        default: Default datetime object. If this is a datetime object and not None,
                elements specified in timestr replace elements in the default object
        ignoretz: If True, time zones in parsed strings are ignored and a naive 
                 datetime.datetime object is returned
        tzinfos: Additional timezone names/aliases that may be present in the string.
                This maps timezone names to actual timezones
        **kwargs: Keyword args passed to _parse()
        
    Returns:
        datetime.datetime object, or if fuzzy_with_tokens=True returns tuple of
        (datetime.datetime, tuple of fuzzy tokens)
        
    Raises:
        ParserError: For invalid/unknown string formats or invalid tzinfo
        TypeError: For non-string/character stream input
        OverflowError: If parsed date exceeds system's largest C integer
    """
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r"
                      % type(timestr).__name__)

    # Handle empty string case
    if not timestr:
        raise ParserError("String cannot be empty")

    # Parse the string using internal _parse method
    res, tokens = self._parse(timestr, **kwargs)

    # If no datetime was found, raise error
    if res is None:
        raise ParserError("Unknown string format: %s" % timestr)

    # Build datetime object from parsed components
    if default is None:
        default = datetime.datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0)

    # Replace any unspecified values with defaults
    for attr in ["year", "month", "day", "hour", 
                "minute", "second", "microsecond"]:
        value = getattr(res, attr, None)
        if value is None:
            setattr(res, attr, getattr(default, attr))

    # Handle timezone if present
    if not ignoretz:
        if res.tzname:
            if tzinfos is None:
                raise ParserError("tzinfos parameter required for %s" % res.tzname)
            
            # Get timezone from tzinfos
            if callable(tzinfos):
                tzdata = tzinfos(res.tzname, res.tzoffset)
            else:
                tzdata = tzinfos.get(res.tzname)
                
            if tzdata is None:
                raise ParserError("Unknown timezone name: %s" % res.tzname)
                
            # Convert tzdata to tzinfo
            if isinstance(tzdata, int):
                tzinfo = tzoffset(res.tzname, tzdata)
            else:
                tzinfo = tzdata
                
            res = res.replace(tzinfo=tzinfo)
            
        elif res.tzoffset:
            res = res.replace(tzinfo=tzoffset(None, res.tzoffset))

    # Return results
    if kwargs.get('fuzzy_with_tokens', False):
        return res, tokens
    else:
        return res