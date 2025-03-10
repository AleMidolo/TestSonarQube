from datetime import datetime, time, timedelta
import pytz

def hydrate_time(nanoseconds, tz=None):
    """
    Idratatore per valori di `Time` e `LocalTime`.

    :param nanoseconds: Il tempo in nanosecondi.
    :param tz: Il fuso orario (timezone) opzionale.
    :return: Un oggetto `datetime.time` rappresentante il tempo.
    """
    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1e9
    
    # Create a timedelta object from the seconds
    delta = timedelta(seconds=seconds)
    
    # Create a base datetime object (e.g., 1970-01-01)
    base_datetime = datetime(1970, 1, 1)
    
    # Add the timedelta to the base datetime
    result_datetime = base_datetime + delta
    
    # Extract the time part
    result_time = result_datetime.time()
    
    # If a timezone is provided, localize the time
    if tz is not None:
        tz = pytz.timezone(tz)
        result_datetime = tz.localize(result_datetime)
        result_time = result_datetime.time()
    
    return result_time