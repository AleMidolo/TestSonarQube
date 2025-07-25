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

    # If timezone is provided, include it in output
    if tz is not None:
        time_components['timezone'] = tz

    return time_components