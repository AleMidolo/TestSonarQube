def from_ticks(cls, ticks, tz=None):
    if not 0 <= ticks < 86400000000000:
        raise ValueError("Ticks must be between 0 and 86400000000000")
        
    # Convert nanoseconds to time components
    nanoseconds = ticks % 1000
    microseconds = (ticks // 1000) % 1000
    total_seconds = ticks // 1000000
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    # Create new Time object with calculated components
    return cls(hours, minutes, seconds, microseconds, nanoseconds, tz)