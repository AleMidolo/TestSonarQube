def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    if default is not None and not isinstance(default, datetime.datetime):
        raise TypeError("Default must be a datetime.datetime object")
        
    # Convert string input to unicode if needed
    if isinstance(timestr, bytes):
        timestr = timestr.decode('ascii')

    if not isinstance(timestr, str):
        raise TypeError("Parser must be given a string or character stream, not a %s" % type(timestr).__name__)

    # Initialize result with default or current time
    res = default or datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    try:
        # Parse the string using internal _parse method
        parsed_result = self._parse(timestr, **kwargs)
        
        if isinstance(parsed_result, tuple):
            # Handle fuzzy_with_tokens case
            dt, tokens = parsed_result
        else:
            dt = parsed_result
            tokens = None

        # Apply timezone info if needed
        if dt.tzinfo is not None and not ignoretz:
            if tzinfos is not None:
                # Handle custom timezone info
                if isinstance(tzinfos, dict):
                    if dt.tzname() in tzinfos:
                        tz = tzinfos[dt.tzname()]
                        if isinstance(tz, int):
                            dt = dt.replace(tzinfo=datetime.timezone(datetime.timedelta(seconds=tz)))
                        else:
                            dt = dt.replace(tzinfo=tz)
                elif callable(tzinfos):
                    dt = dt.replace(tzinfo=tzinfos(dt.tzname(), dt.utcoffset()))
        elif ignoretz:
            dt = dt.replace(tzinfo=None)

        # Merge with default
        if default is not None:
            # Replace any unspecified components with defaults
            current = {
                'year': dt.year if dt.year != 1900 else default.year,
                'month': dt.month if dt.month != 1 else default.month,
                'day': dt.day if dt.day != 1 else default.day,
                'hour': dt.hour if dt.hour != 0 else default.hour,
                'minute': dt.minute if dt.minute != 0 else default.minute,
                'second': dt.second if dt.second != 0 else default.second,
                'microsecond': dt.microsecond if dt.microsecond != 0 else default.microsecond,
            }
            dt = dt.replace(**current)

        if tokens is not None:
            return dt, tokens
        return dt

    except ValueError as e:
        raise ParserError(str(e))
    except OverflowError as e:
        raise OverflowError("Parsed date exceeds the largest valid C integer on your system")