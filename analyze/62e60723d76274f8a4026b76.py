def from_ticks(cls, ticks, tz=None):
    if not 0 <= ticks < 86400000000000:
        raise ValueError("Ticks must be between 0 and 86400000000000")
        
    # Convert nanoseconds to time components
    nanoseconds = ticks % 1000
    ticks //= 1000
    
    microseconds = ticks % 1000
    ticks //= 1000
    
    milliseconds = ticks % 1000
    ticks //= 1000
    
    total_seconds = ticks
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    # Create time object with calculated components
    return cls(hours, minutes, seconds, microseconds=microseconds*1000 + nanoseconds//1000, tzinfo=tz)