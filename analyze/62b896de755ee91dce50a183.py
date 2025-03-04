def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse string into datetime object."""
    
    if default is not None and not isinstance(default, datetime.datetime):
        raise TypeError("Default must be a datetime.datetime object")
        
    # Handle non-string input
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream")
        
    # Remove leading/trailing whitespace
    timestr = timestr.strip()
    
    try:
        # Parse the string using internal _parse method
        res, tokens = self._parse(timestr, **kwargs)
        
        if res is None:
            raise ParserError("String does not contain a date.")
            
        # If default is provided, replace any unspecified items
        if default:
            repl = {}
            for attr in ["year", "month", "day", "hour", 
                        "minute", "second", "microsecond"]:
                if getattr(res, attr) is None:
                    repl[attr] = getattr(default, attr)
            res = res.replace(**repl)
            
        # Handle timezone information
        if not ignoretz:
            # Get timezone info if present
            tz = res.tzinfo
            
            # Use tzinfos if provided
            if tzinfos is not None and isinstance(tzinfos, dict):
                if tz.tzname in tzinfos:
                    newtz = tzinfos[tz.tzname]
                    if isinstance(newtz, int):
                        newtz = tzoffset(tz.tzname, newtz)
                    res = res.replace(tzinfo=newtz)
            elif callable(tzinfos):
                res = res.replace(tzinfo=tzinfos(tz.tzname, tz.utcoffset()))
        else:
            # Remove timezone if ignoretz=True
            res = res.replace(tzinfo=None)
            
        if kwargs.get('fuzzy_with_tokens', False):
            return res, tokens
        else:
            return res
            
    except (ValueError, OverflowError) as e:
        raise ParserError(str(e))