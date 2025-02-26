from datetime import datetime, timedelta, timezone

def hydrate_time(nanoseconds, tz=None):
    """
    `Time` और `LocalTime` मानों के लिए हाइड्रेटर।  

    पैरामीटर (Parameters):
    - nanoseconds: 
    - tz: 

    वापसी मान:
    - समय 
    """
    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1_000_000_000
    # Create a UTC datetime object
    utc_time = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=seconds)
    
    if tz is not None:
        # Convert to the specified timezone
        local_time = utc_time.astimezone(tz)
        return local_time
    return utc_time