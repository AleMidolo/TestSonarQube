def hydrate_time(nanoseconds, tz=None):
    """
    `Time` और `LocalTime` मानों के लिए हाइड्रेटर।  

    पैरामीटर (Parameters):
    -nanoseconds: 
    - tz: 

    वापसी मान:
    - समय 
    """
    # Convert nanoseconds to hours, minutes, seconds, nanoseconds
    total_seconds = nanoseconds // 1_000_000_000
    remaining_nanos = nanoseconds % 1_000_000_000
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Format time components
    if tz is None:
        # Return time without timezone
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{remaining_nanos:09d}"
    else:
        # Return time with timezone
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{remaining_nanos:09d} {tz}"

    return time_str