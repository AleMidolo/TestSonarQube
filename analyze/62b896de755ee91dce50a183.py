def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse date/time string to datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % type(timestr))
        
    # Default datetime object to use for missing values
    default_datetime = default or datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    try:
        # Parse the string into components
        res = self._parse(timestr, **kwargs)
        
        if res is None:
            raise ParserError("Unknown string format: %s" % timestr)
            
        # Get timezone info if needed
        if not ignoretz:
            tz = None
            # Check for timezone in parsed result
            if res.tzname:
                # Use tzinfos if provided
                if tzinfos:
                    if callable(tzinfos):
                        tz = tzinfos(res.tzname, res.tzoffset)
                    else:
                        tz = tzinfos.get(res.tzname)
                # Use offset if available
                elif res.tzoffset is not None:
                    tz = datetime.timezone(datetime.timedelta(seconds=res.tzoffset))
                    
        # Build datetime object
        year = res.year if res.year is not None else default_datetime.year
        month = res.month if res.month is not None else default_datetime.month
        day = res.day if res.day is not None else default_datetime.day
        hour = res.hour if res.hour is not None else default_datetime.hour
        minute = res.minute if res.minute is not None else default_datetime.minute
        second = res.second if res.second is not None else default_datetime.second
        microsecond = res.microsecond if res.microsecond is not None else default_datetime.microsecond
        
        try:
            dt = datetime.datetime(year, month, day, hour, minute, second, microsecond)
            
            # Add timezone if needed
            if not ignoretz and tz is not None:
                dt = dt.replace(tzinfo=tz)
                
            # Return parsed datetime
            if kwargs.get('fuzzy_with_tokens', False):
                return dt, res.tokens
            return dt
            
        except (ValueError, OverflowError) as e:
            raise ParserError(str(e))
            
    except Exception as e:
        raise ParserError("Unknown string format: %s" % timestr)