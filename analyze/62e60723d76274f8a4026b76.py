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
    if not (0 <= ticks < 86400000000000):
        raise ValueError("Ticks must be between 0 and 86400000000000.")
    
    seconds = ticks // 1_000_000_000
    nanoseconds = ticks % 1_000_000_000
    
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    
    time_obj = cls(hour=hours, minute=minutes, second=seconds, microsecond=nanoseconds // 1000, tzinfo=tz)
    
    return time_obj