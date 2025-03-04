def hydrate_time(nanoseconds, tz=None):
    """
    `Time` और `LocalTime` मानों के लिए हाइड्रेटर।  

    पैरामीटर (Parameters):
    -nanoseconds: 
    - tz: 

    वापसी मान:
    - समय 
    """
    # Convert nanoseconds to hours, minutes, seconds
    total_seconds = nanoseconds // 1_000_000_000
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    nanos = nanoseconds % 1_000_000_000

    # Create time components
    time_components = {
        'hour': int(hours % 24),
        'minute': int(minutes),
        'second': int(seconds),
        'nanosecond': int(nanos)
    }

    if tz is not None:
        # If timezone is provided, return localized time
        from datetime import datetime, timezone
        from zoneinfo import ZoneInfo
        
        dt = datetime.now(ZoneInfo(tz))
        time_components['tzinfo'] = dt.tzinfo
        
        from datetime import time
        return time(**time_components)
    else:
        # Return naive time
        from datetime import time
        return time(**time_components)