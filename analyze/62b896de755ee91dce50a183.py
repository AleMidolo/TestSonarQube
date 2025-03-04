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
        raise ParserError("String is empty")
        
    try:
        # Call internal _parse method with all arguments
        res, tokens = self._parse(timestr, default=default, ignoretz=ignoretz,
                                tzinfos=tzinfos, **kwargs)
            
        # If fuzzy_with_tokens is True, return tuple of (datetime, tokens)
        if kwargs.get('fuzzy_with_tokens', False):
            return res, tokens
            
        return res
        
    except Exception as e:
        # Convert parsing exceptions to ParserError
        raise ParserError(str(e))