from datetime import time, timedelta
import pytz

def hydrate_time(nanoseconds, tz=None):
    """
    Idratatore per valori di `Time` e `LocalTime`.

    :param nanoseconds: Il tempo in nanosecondi.
    :param tz: Il fuso orario (timezone) opzionale.
    :return: Un oggetto `time` o `datetime.time` con il fuso orario specificato.
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
        time_obj = tz_obj.localize(time_obj)
    
    return time_obj