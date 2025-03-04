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
    remaining_ns = ticks % ns_per_second
    
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    microseconds = int(remaining_ns // ns_per_microsecond)
    
    return cls(hours, minutes, seconds, microseconds, tzinfo=tz)