def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    if default is not None and not isinstance(default, datetime.datetime):
        raise TypeError("Default must be a datetime.datetime object")
        
    # Convert string input to unicode if needed
    if isinstance(timestr, bytes):
        timestr = timestr.decode('ascii')

    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not "
                      f"{type(timestr).__name__}")

    # Initialize result with default or current time
    res = default or datetime.datetime.now().replace(hour=0, minute=0, second=0,
                                                   microsecond=0)

    try:
        # Parse the string using internal _parse method
        parsed = self._parse(timestr, **kwargs)
        
        if parsed is None:
            raise ParserError("Unknown string format")
            
        # Handle fuzzy parsing if enabled
        if kwargs.get('fuzzy_with_tokens', False):
            dt, tokens = parsed
        else:
            dt = parsed
            tokens = None
            
        # Apply timezone handling
        if dt.tzinfo is not None and ignoretz:
            dt = dt.replace(tzinfo=None)
        elif dt.tzinfo is None and tzinfos and not ignoretz:
            # Try to get timezone from tzinfos
            if isinstance(tzinfos, dict):
                if dt.tzname() in tzinfos:
                    tz = tzinfos[dt.tzname()]
                    if isinstance(tz, numbers.Number):
                        dt = dt.replace(tzinfo=tzoffset(dt.tzname(), tz))
                    else:
                        dt = dt.replace(tzinfo=tz)
            elif callable(tzinfos):
                tz = tzinfos(dt.tzname(), dt.utcoffset() and dt.utcoffset().total_seconds())
                dt = dt.replace(tzinfo=tz)
                
        # Return parsed datetime
        if kwargs.get('fuzzy_with_tokens', False):
            return dt, tokens
        return dt
        
    except (TypeError, ValueError, OverflowError) as e:
        raise ParserError(f"Unknown string format: {str(e)}")