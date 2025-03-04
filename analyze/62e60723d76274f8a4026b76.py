def from_ticks(cls, ticks, tz=None):
    """
    Crear una hora a partir de ticks (nanosegundos desde la medianoche).

    :param ticks: nanosegundos desde la medianoche 
    :type ticks: int
    :param tz: zona horaria opcional
    :type tz: datetime.tzinfo

    :rtype: Time

    :raises ValueError: si los ticks están fuera de los límites
        (0 <= ticks < 86400000000000)
    """
    if not 0 <= ticks < 86400000000000:
        raise ValueError("Ticks must be between 0 and 86400000000000")
        
    # Convert nanoseconds to hours, minutes, seconds, microseconds
    total_microseconds = ticks // 1000
    hours = total_microseconds // 3600000000
    remaining = total_microseconds % 3600000000
    minutes = remaining // 60000000
    remaining = remaining % 60000000
    seconds = remaining // 1000000
    microseconds = remaining % 1000000
    
    # Create Time object using the calculated components
    return cls(hour=int(hours), 
              minute=int(minutes), 
              second=int(seconds),
              microsecond=int(microseconds), 
              tzinfo=tz)