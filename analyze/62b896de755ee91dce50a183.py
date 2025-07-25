def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse date/time string to datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % type(timestr))
        
    # Default datetime object to use for missing values
    default_datetime = default or datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    try:
        # Parse the string using _parse() internal method
        res, tokens = self._parse(timestr, **kwargs)
        
        if res is None:
            raise ParserError("Unknown string format: %s" % timestr)
            
        # Convert parsed elements to datetime object
        if len(res) == 0:
            raise ParserError("String does not contain any date/time information")
            
        year = res.get('year', default_datetime.year)
        month = res.get('month', default_datetime.month) 
        day = res.get('day', default_datetime.day)
        hour = res.get('hour', default_datetime.hour)
        minute = res.get('minute', default_datetime.minute)
        second = res.get('second', default_datetime.second)
        microsecond = res.get('microsecond', default_datetime.microsecond)
        
        # Handle timezone
        tzname = res.get('tzname')
        tzoffset = res.get('tzoffset')
        tz = None
        
        if not ignoretz:
            if tzname is not None:
                if tzinfos is not None:
                    if callable(tzinfos):
                        tz = tzinfos(tzname, tzoffset)
                    else:
                        tz = tzinfos.get(tzname)
                        
            elif tzoffset is not None:
                tz = datetime.timezone(datetime.timedelta(seconds=tzoffset))
                
        try:
            dt = datetime.datetime(year, month, day, hour, minute, second,
                                 microsecond, tzinfo=tz)
        except ValueError as e:
            raise ParserError(str(e))
        except OverflowError as e:
            raise OverflowError(str(e))
            
        if kwargs.get('fuzzy_with_tokens', False):
            return dt, tokens
        return dt
        
    except Exception as e:
        raise ParserError("Unknown string format: %s" % timestr) from e