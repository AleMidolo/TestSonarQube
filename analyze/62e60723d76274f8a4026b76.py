def from_ticks(cls, ticks, tz=None):
    """
    Create a time from ticks (nanoseconds since midnight).

    :param ticks: nanoseconds since midnight
    :type ticks: int
    :param tz: optional timezone
    :type tz: datetime.tzinfo

    :rtype: Time

    :raises ValueError: if ticks is out of bounds
        (0 <= ticks < 86400000000000)
    """
    if not 0 <= ticks < 86400000000000:
        raise ValueError("Ticks must be between 0 and 86400000000000")
        
    # Convert nanoseconds to hours, minutes, seconds, microseconds
    ns_per_second = 1000000000
    ns_per_microsecond = 1000
    
    total_seconds = ticks // ns_per_second
    nanoseconds = ticks % ns_per_second
    microseconds = nanoseconds // ns_per_microsecond
    
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return cls(hours, minutes, seconds, microseconds, tz)