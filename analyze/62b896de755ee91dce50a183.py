def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse date/time string to datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % timestr)
        
    # Default handling
    if default is not None and not isinstance(default, datetime.datetime):
        raise TypeError("Default must be a datetime.datetime object")
        
    res = None
    
    try:
        # Parse the string using _parse() internal method
        res, tokens = self._parse(timestr, **kwargs)
        
        if res is None:
            raise ParserError("Unknown string format: %s" % timestr)
            
        # If default is provided, replace any unspecified items
        if default is not None:
            repl = {}
            for attr in ["year", "month", "day", "hour", "minute", "second", "microsecond"]:
                if getattr(res, attr) is None:
                    repl[attr] = getattr(default, attr)
            res = res.replace(**repl)
            
        # Handle timezone
        if not ignoretz:
            if res.tzinfo is None and tzinfos is not None:
                # Try to get timezone from tzinfos
                tz = None
                if isinstance(tzinfos, collections.Callable):
                    try:
                        tz = tzinfos(res.tzname, res.tzoffset)
                    except:
                        pass
                elif res.tzname in tzinfos:
                    tz = tzinfos[res.tzname]
                    
                # Convert tz to proper timezone object if needed
                if isinstance(tz, (int, float)):
                    tz = datetime.timezone(datetime.timedelta(seconds=tz))
                    
                if tz is not None:
                    res = res.replace(tzinfo=tz)
                    
        elif ignoretz:
            # Remove timezone if ignoretz is True
            res = res.replace(tzinfo=None)
            
        # Return results based on fuzzy_with_tokens setting
        if kwargs.get('fuzzy_with_tokens', False):
            return res, tokens
        else:
            return res
            
    except ValueError as e:
        raise ParserError(str(e))
    except OverflowError as e:
        raise OverflowError(str(e))