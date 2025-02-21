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
    if not (0 <= ticks < 86400000000000):
        raise ValueError("Ticks must be between 0 and 86400000000000")
    
    seconds = ticks // 1_000_000_000
    nanoseconds = ticks % 1_000_000_000
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    time_instance = cls(hours, minutes, seconds, nanoseconds, tz)
    return time_instance