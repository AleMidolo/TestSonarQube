def from_ticks(cls, ticks, tz=None):
    """
    Crea un'istanza di tempo a partire dai ticks (nanosecondi trascorsi dalla mezzanotte).

    :param ticks: nanosecondi trascorsi dalla mezzanotte
    :type ticks: int
    :param tz: fuso orario opzionale
    :type tz: datetime.tzinfo

    :rtype: Time

    :raises ValueError: se il valore di ticks è fuori dai limiti
        (0 <= ticks < 86400000000000)
    """
    if not 0 <= ticks < 86400000000000:
        raise ValueError("Ticks value must be between 0 and 86400000000000")
        
    # Convert nanoseconds to hours, minutes, seconds, microseconds
    total_microseconds = ticks // 1000
    hours = total_microseconds // 3600000000
    remaining = total_microseconds % 3600000000
    minutes = remaining // 60000000
    remaining = remaining % 60000000
    seconds = remaining // 1000000
    microseconds = remaining % 1000000
    
    # Create new Time instance
    return cls(hours, minutes, seconds, microseconds, tz)