from datetime import time, timedelta
from pytz import timezone

def hydrate_time(nanoseconds, tz=None):
    """
    Hidratador para valores de `Time` y `LocalTime`.

    :param nanoseconds: El número de nanosegundos desde la medianoche.
    :param tz: La zona horaria (opcional).
    :return: Un objeto `time` o `datetime.time` con la zona horaria aplicada.
    """
    # Convert nanoseconds to seconds and microseconds
    seconds = nanoseconds // 1_000_000_000
    microseconds = (nanoseconds % 1_000_000_000) // 1000
    
    # Create a time object
    t = time(second=seconds % 60, minute=(seconds // 60) % 60, hour=(seconds // 3600) % 24, microsecond=microseconds)
    
    if tz:
        # Apply timezone if provided
        tz_obj = timezone(tz)
        # Create a dummy datetime to apply the timezone
        dummy_datetime = datetime.datetime(1970, 1, 1, t.hour, t.minute, t.second, t.microsecond)
        localized_time = tz_obj.localize(dummy_datetime).timetz()
        return localized_time
    else:
        return t