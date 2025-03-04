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
    
    seconds = ticks % 60
    ticks //= 60
    
    minutes = ticks % 60
    hours = ticks // 60

    # Create time object with calculated components
    return cls(hours, minutes, seconds, 
              milliseconds=milliseconds,
              microseconds=microseconds, 
              nanoseconds=nanoseconds,
              tzinfo=tz)