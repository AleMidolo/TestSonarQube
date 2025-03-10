from datetime import time, timedelta
import pytz

def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds: El tiempo en nanosegundos desde la medianoche.
    :param tz: La zona horaria (opcional).
    :return: Un objeto `time` o `datetime.time` con la zona horaria aplicada si se proporciona.
    """
    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1e9
    
    # Calculate hours, minutes, seconds, and microseconds
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds %= 60
    microseconds = int((seconds - int(seconds)) * 1e6)
    seconds = int(seconds)
    
    # Create a time object
    time_obj = time(hour=hours, minute=minutes, second=seconds, microsecond=microseconds)
    
    if tz:
        # If a timezone is provided, localize the time
        tz_obj = pytz.timezone(tz)
        dt = datetime.combine(datetime.today(), time_obj)
        localized_dt = tz_obj.localize(dt)
        return localized_dt.time()
    
    return time_obj