def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse date/time string to datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % timestr)
        
    # Default datetime object to use for missing values
    default_datetime = default or datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    try:
        # Parse the string using _parse() internal method
        res, tokens = self._parse(timestr, **kwargs)
        
        if res is None:
            raise ParserError("Unknown string format: %s" % timestr)
            
        # Convert parsed elements to datetime
        year = res.year if res.year is not None else default_datetime.year
        month = res.month if res.month is not None else default_datetime.month
        day = res.day if res.day is not None else default_datetime.day
        hour = res.hour if res.hour is not None else default_datetime.hour
        minute = res.minute if res.minute is not None else default_datetime.minute
        second = res.second if res.second is not None else default_datetime.second
        microsecond = res.microsecond if res.microsecond is not None else default_datetime.microsecond
        
        # Handle timezone
        tzinfo = None
        if not ignoretz:
            if res.tzname:
                if tzinfos:
                    if callable(tzinfos):
                        tzinfo = tzinfos(res.tzname, res.tzoffset)
                    else:
                        if res.tzname in tzinfos:
                            tzinfo = tzinfos[res.tzname]
                            if isinstance(tzinfo, numbers.Number):
                                tzinfo = datetime.timezone(datetime.timedelta(seconds=tzinfo))
                elif res.tzoffset:
                    tzinfo = datetime.timezone(datetime.timedelta(seconds=res.tzoffset))
                    
        try:
            dt = datetime.datetime(year, month, day, hour, minute, second,
                                 microsecond, tzinfo=tzinfo)
        except ValueError as e:
            raise ParserError(str(e))
            
        if kwargs.get('fuzzy_with_tokens', False):
            return dt, tokens
        return dt
        
    except (TypeError, ValueError, OverflowError) as e:
        raise ParserError(str(e))