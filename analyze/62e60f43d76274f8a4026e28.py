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
    
    # Create a time object
    t = time(second=seconds, microsecond=microseconds)
    
    if tz:
        # If a timezone is provided, localize the time
        tz_obj = pytz.timezone(tz)
        dt = datetime.combine(datetime.today(), t)
        localized_dt = tz_obj.localize(dt)
        return localized_dt.time()
    
    return t