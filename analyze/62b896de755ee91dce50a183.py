def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """
    Parse a datetime string into a datetime.datetime object.
    
    Args:
        timestr: Any datetime string using supported formats
        default: Default datetime object. If this is a datetime object and not None,
                elements specified in timestr replace elements in the default object
        ignoretz: If True, time zones in parsed strings are ignored and a naive 
                 datetime.datetime object is returned
        tzinfos: Additional timezone names/aliases that may be present in the string
        **kwargs: Keyword args passed to _parse()
        
    Returns:
        datetime.datetime object, or if fuzzy_with_tokens=True, returns tuple of
        (datetime.datetime, tuple of fuzzy tokens)
        
    Raises:
        ParserError: For invalid/unknown string formats, invalid tzinfo, or invalid dates
        TypeError: For non-string/character stream input
        OverflowError: If parsed date exceeds system's largest C integer
    """
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % timestr)
        
    # Handle empty string case
    if not timestr:
        raise ParserError("String is empty")
        
    # Parse the string using internal _parse method
    res, tokens = self._parse(timestr, **kwargs)
    
    if res is None:
        raise ParserError("Unknown string format: %s" % timestr)
        
    # If default is provided, replace any unspecified items
    if default is not None:
        repl = {}
        for attr in ["year", "month", "day", "hour", "minute", "second", "microsecond"]:
            value = getattr(res, attr)
            if value is None:
                repl[attr] = getattr(default, attr)
        res = res.replace(**repl)
        
    # Handle timezone info
    if not ignoretz:
        if tzinfos is not None:
            # Apply custom timezone info
            if isinstance(tzinfos, dict):
                if res.tzname in tzinfos:
                    tzinfo = tzinfos[res.tzname]
                    if isinstance(tzinfo, int):
                        tzinfo = tzoffset(res.tzname, tzinfo)
                    res = res.replace(tzinfo=tzinfo)
            else:
                # tzinfos is a function
                try:
                    tzinfo = tzinfos(res.tzname, res.tzoffset)
                    res = res.replace(tzinfo=tzinfo)
                except Exception:
                    pass
    else:
        # Strip timezone if ignoretz=True
        res = res.replace(tzinfo=None)
            
    # Return results based on fuzzy_with_tokens setting
    if kwargs.get('fuzzy_with_tokens', False):
        return res, tokens
    else:
        return res