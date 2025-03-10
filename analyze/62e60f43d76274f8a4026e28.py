from datetime import time, timedelta
import pytz

def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds: El tiempo en nanosegundos.
    :param tz: La zona horaria (opcional).
    :return: Un objeto `time` o `datetime.time` con la zona horaria aplicada si se proporciona.
    """
    # Convert nanoseconds to seconds and microseconds
    seconds = nanoseconds // 1_000_000_000
    microseconds = (nanoseconds % 1_000_000_000) // 1000
    
    # Create a timedelta object to represent the time
    delta = timedelta(seconds=seconds, microseconds=microseconds)
    
    # Create a time object from the timedelta
    t = (datetime.min + delta).time()
    
    if tz:
        # If a timezone is provided, localize the time
        tz_obj = pytz.timezone(tz)
        t = tz_obj.localize(datetime.combine(datetime.today(), t)).time()
    
    return t