from datetime import time, timedelta
import pytz

def hydrate_time(nanoseconds, tz=None):
    """
    Hydrator for `Time` and `LocalTime` values.

    :param nanoseconds: The time in nanoseconds.
    :param tz: The timezone (optional).
    :return: Time object.
    """
    # Convert nanoseconds to seconds and microseconds
    seconds = nanoseconds // 1_000_000_000
    microseconds = (nanoseconds % 1_000_000_000) // 1000
    
    # Create a timedelta object to represent the time
    delta = timedelta(seconds=seconds, microseconds=microseconds)
    
    # Create a time object from the timedelta
    time_obj = (time.min + delta).time()
    
    # If a timezone is provided, localize the time
    if tz is not None:
        tz = pytz.timezone(tz)
        time_obj = tz.localize(time_obj)
    
    return time_obj