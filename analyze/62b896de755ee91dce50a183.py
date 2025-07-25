def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse a date/time string into a datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % timestr)
        
    # Default handling
    if default is not None and not isinstance(default, datetime):
        raise TypeError("Default must be a datetime.datetime object")
        
    # Parse the string using _parse() internal method
    res, tokens = self._parse(timestr, **kwargs)
    
    if res is None:
        raise ParserError("Unknown string format: %s" % timestr)
        
    # Build datetime object from parsed components
    try:
        year = res.year if res.year is not None else default.year if default else None
        month = res.month if res.month is not None else default.month if default else None  
        day = res.day if res.day is not None else default.day if default else None
        hour = res.hour if res.hour is not None else default.hour if default else 0
        minute = res.minute if res.minute is not None else default.minute if default else 0
        second = res.second if res.second is not None else default.second if default else 0
        microsecond = res.microsecond if res.microsecond is not None else default.microsecond if default else 0
        
        if year is None or month is None or day is None:
            raise ParserError("Required date fields not found")
            
        aware_dt = datetime(year, month, day, hour, minute, second, microsecond)
        
        # Handle timezone
        if not ignoretz:
            if res.tzname:
                if tzinfos is None:
                    raise ParserError("tzinfos parameter required for %s" % res.tzname)
                    
                if isinstance(tzinfos, dict):
                    tz = tzinfos.get(res.tzname)
                else:
                    tz = tzinfos(res.tzname, res.tzoffset)
                    
                if isinstance(tz, int):
                    aware_dt = aware_dt.replace(tzinfo=tzoffset(res.tzname, tz))
                elif hasattr(tz, 'localize'):
                    aware_dt = tz.localize(aware_dt)
                else:
                    aware_dt = aware_dt.replace(tzinfo=tz)
            elif res.tzoffset is not None:
                aware_dt = aware_dt.replace(tzinfo=tzoffset(None, res.tzoffset))
                
        elif ignoretz:
            aware_dt = aware_dt.replace(tzinfo=None)
            
        # Return results
        if kwargs.get('fuzzy_with_tokens', False):
            return aware_dt, tokens
        else:
            return aware_dt
            
    except (TypeError, ValueError) as e:
        raise ParserError(str(e))
    except OverflowError as e:
        raise OverflowError(str(e))