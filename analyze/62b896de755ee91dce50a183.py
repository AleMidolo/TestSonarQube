def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse date/time string to datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % timestr)
        
    # Default handling
    if default is not None and not isinstance(default, datetime.datetime):
        raise TypeError("Default must be a datetime.datetime object")
        
    res = self._parse(timestr, **kwargs)
    
    if res is None:
        raise ParserError("Unknown string format: %s" % timestr)
        
    # Extract datetime components
    year = res.year if res.year is not None else default.year if default else None
    month = res.month if res.month is not None else default.month if default else None  
    day = res.day if res.day is not None else default.day if default else None
    hour = res.hour if res.hour is not None else default.hour if default else 0
    minute = res.minute if res.minute is not None else default.minute if default else 0
    second = res.second if res.second is not None else default.second if default else 0
    microsecond = res.microsecond if res.microsecond is not None else default.microsecond if default else 0
    
    if None in (year, month, day):
        raise ParserError("Required date fields not found")
        
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
                if tzinfo is not None and not isinstance(tzinfo, datetime.tzinfo):
                    tzinfo = datetime.timezone(datetime.timedelta(seconds=tzinfo))
            elif res.tzoffset is not None:
                tzinfo = datetime.timezone(datetime.timedelta(seconds=res.tzoffset))
                
    try:
        return datetime.datetime(year, month, day, hour, minute, second,
                               microsecond, tzinfo=tzinfo)
    except (ValueError, OverflowError) as e:
        raise ParserError(str(e))