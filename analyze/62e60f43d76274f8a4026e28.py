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
    # Create a datetime object from the epoch
    time = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=seconds)
    
    # If a timezone is provided, convert the time to that timezone
    if tz is not None:
        time = time.astimezone(tz)
    
    return time