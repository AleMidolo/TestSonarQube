from datetime import time, timedelta
import pytz

def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds: El número de nanosegundos desde la medianoche.
    :param tz: La zona horaria (opcional).
    :return: Un objeto `time` o `datetime.time` con la zona horaria aplicada si se proporciona.
    """
    # Convert nanoseconds to seconds and microseconds
    seconds = nanoseconds // 1_000_000_000
    microseconds = (nanoseconds % 1_000_000_000) // 1000
    
    # Create a timedelta to represent the time since midnight
    delta = timedelta(seconds=seconds, microseconds=microseconds)
    
    # Create a time object from the timedelta
    t = (time.min + delta).time()
    
    # Apply timezone if provided
    if tz is not None:
        tz = pytz.timezone(tz)
        t = tz.localize(t)
    
    return t