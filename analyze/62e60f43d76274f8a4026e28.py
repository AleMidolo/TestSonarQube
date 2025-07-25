from datetime import datetime, timezone, timedelta

def hydrate_time(nanoseconds, tz=None):
    """
    `Time` और `LocalTime` मानों के लिए हाइड्रेटर।  

    पैरामीटर (Parameters):
    - nanoseconds: समय को नैनोसेकंड में दर्शाने वाला पूर्णांक
    - tz: समय क्षेत्र (timezone) जो datetime.timezone या str हो सकता है

    वापसी मान:
    - समय (datetime.datetime ऑब्जेक्ट)
    """
    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1e9
    
    # Create a datetime object from the timestamp
    dt = datetime.fromtimestamp(seconds, tz=timezone.utc)
    
    # If a timezone is provided, convert the datetime to that timezone
    if tz is not None:
        if isinstance(tz, str):
            from pytz import timezone as pytz_timezone
            tz = pytz_timezone(tz)
        dt = dt.astimezone(tz)
    
    return dt