def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse a date/time string into a datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % timestr)
        
    # Default datetime object to use for missing values
    default_datetime = datetime.datetime.now() if default is None else default
    
    try:
        # Parse the string using _parse() internal method
        res, tokens = self._parse(timestr, **kwargs)
        
        if res is None:
            raise ParserError("Unknown string format: %s" % timestr)
            
        # Get year, month, day values
        year = res.year if res.year is not None else default_datetime.year
        month = res.month if res.month is not None else default_datetime.month
        day = res.day if res.day is not None else default_datetime.day
        
        # Get time values
        hour = res.hour if res.hour is not None else default_datetime.hour
        minute = res.minute if res.minute is not None else default_datetime.minute
        second = res.second if res.second is not None else default_datetime.second
        microsecond = res.microsecond if res.microsecond is not None else default_datetime.microsecond
        
        # Handle timezone
        if ignoretz:
            tzinfo = None
        else:
            tzinfo = res.tzinfo
            
            # Use tzinfos if provided
            if tzinfo is not None and tzinfos is not None:
                if isinstance(tzinfos, dict):
                    if tzinfo in tzinfos:
                        tzinfo = tzinfos[tzinfo]
                elif callable(tzinfos):
                    tzinfo = tzinfos(tzinfo, res.tzoffset)
                    
        try:
            return datetime.datetime(year, month, day, hour, minute, second,
                                   microsecond, tzinfo=tzinfo)
        except ValueError as e:
            raise ParserError(str(e))
        except OverflowError as e:
            raise OverflowError(str(e))
            
    except Exception as e:
        raise ParserError("Unknown string format: %s" % timestr)