def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse a date/time string into a datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % timestr)
        
    # Default handling
    if default is not None and not isinstance(default, datetime):
        raise TypeError("Default must be a datetime.datetime object")
        
    res = self._parse(timestr, **kwargs)
    
    if res is None:
        raise ParserError("Unknown string format: %s" % timestr)
        
    # Extract datetime components from parsed result
    year = res.year if res.year is not None else default.year if default else None
    month = res.month if res.month is not None else default.month if default else None 
    day = res.day if res.day is not None else default.day if default else None
    hour = res.hour if res.hour is not None else default.hour if default else 0
    minute = res.minute if res.minute is not None else default.minute if default else 0
    second = res.second if res.second is not None else default.second if default else 0
    microsecond = res.microsecond if res.microsecond is not None else default.microsecond if default else 0
    
    if year is None or month is None or day is None:
        raise ParserError("Required date fields not found")
        
    # Handle timezone
    tzinfo = None
    if not ignoretz:
        if res.tzname:
            if tzinfos is None:
                raise ParserError("tzinfos parameter required for %s" % res.tzname)
                
            if isinstance(tzinfos, dict):
                if res.tzname in tzinfos:
                    tzinfo = tzinfos[res.tzname]
                    if isinstance(tzinfo, int):
                        tzinfo = tzoffset(res.tzname, tzinfo)
            else:
                try:
                    tzinfo = tzinfos(res.tzname, res.tzoffset)
                except Exception:
                    raise ParserError("Invalid tzinfo provided")
                    
        elif res.tzoffset is not None:
            tzinfo = tzoffset(None, res.tzoffset)
            
    try:
        return datetime(year, month, day, hour, minute, second, 
                       microsecond, tzinfo=tzinfo)
    except (ValueError, OverflowError) as e:
        raise ParserError(str(e))