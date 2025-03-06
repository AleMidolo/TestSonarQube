from datetime import datetime, time, timedelta
import pytz

def hydrate_time(nanoseconds, tz=None):
    """
    Idratatore per valori di `Time` e `LocalTime`.

    :param nanoseconds: Il tempo in nanosecondi.
    :param tz: Il fuso orario (opzionale).
    :return: Un oggetto `datetime.time` rappresentante il tempo.
    """
    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1e9
    
    # Create a timedelta object from the seconds
    delta = timedelta(seconds=seconds)
    
    # Create a datetime object starting from epoch (1970-01-01)
    epoch = datetime(1970, 1, 1)
    dt = epoch + delta
    
    # Extract the time part
    time_obj = dt.time()
    
    # If a timezone is provided, localize the time
    if tz:
        tz_obj = pytz.timezone(tz)
        dt = tz_obj.localize(dt)
        time_obj = dt.time()
    
    return time_obj