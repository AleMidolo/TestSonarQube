def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """Parse a date/time string into a datetime.datetime object."""
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not %r" % timestr)
        
    # Default datetime object to use for missing values
    default_datetime = default or datetime.datetime.now()
    
    try:
        # Parse the string using internal _parse method
        res, tokens = self._parse(timestr, **kwargs)
        
        # If fuzzy_with_tokens is True, return both datetime and tokens
        if kwargs.get('fuzzy_with_tokens', False):
            return res, tokens
            
        year = res.year if res.year is not None else default_datetime.year
        month = res.month if res.month is not None else default_datetime.month
        day = res.day if res.day is not None else default_datetime.day
        hour = res.hour if res.hour is not None else default_datetime.hour
        minute = res.minute if res.minute is not None else default_datetime.minute
        second = res.second if res.second is not None else default_datetime.second
        microsecond = res.microsecond if res.microsecond is not None else default_datetime.microsecond
        
        if res.tzname is not None and not ignoretz:
            # Handle timezone
            if tzinfos is not None:
                # Use provided timezone info
                if callable(tzinfos):
                    tzinfo = tzinfos(res.tzname, res.tzoffset)
                else:
                    if res.tzname in tzinfos:
                        tzinfo = tzinfos[res.tzname]
                        if isinstance(tzinfo, int):
                            tzinfo = datetime.timezone(datetime.timedelta(seconds=tzinfo))
                    else:
                        raise ParserError(f"Unknown timezone name: {res.tzname}")
            else:
                # Create timezone from offset
                if res.tzoffset is not None:
                    tzinfo = datetime.timezone(datetime.timedelta(seconds=res.tzoffset))
                else:
                    raise ParserError(f"Timezone offset not found for: {res.tzname}")
        else:
            tzinfo = None if ignoretz else default_datetime.tzinfo
            
        try:
            return datetime.datetime(year, month, day, hour, minute, second,
                                   microsecond, tzinfo=tzinfo)
        except (ValueError, OverflowError) as e:
            raise ParserError(str(e))
            
    except Exception as e:
        raise ParserError("Unknown string format: %s" % timestr) from e