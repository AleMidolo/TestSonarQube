import datetime

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
        raise ValueError("Ticks fuera de los límites (0 <= ticks < 86400000000000)")
    
    nanoseconds_per_second = 1_000_000_000
    seconds = ticks // nanoseconds_per_second
    nanoseconds = ticks % nanoseconds_per_second
    
    time = datetime.time(seconds // 3600, (seconds % 3600) // 60, seconds % 60, nanoseconds // 1000, tzinfo=tz)
    
    return time