def from_ticks(cls, ticks, tz=None):
    if not (0 <= ticks < 86400000000000):
        raise ValueError("Ticks must be in the range [0, 86400000000000)")
    
    seconds = ticks // 1_000_000_000
    nanoseconds = ticks % 1_000_000_000
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    time_obj = cls(hour=hours, minute=minutes, second=seconds, microsecond=nanoseconds // 1000, tzinfo=tz)
    return time_obj