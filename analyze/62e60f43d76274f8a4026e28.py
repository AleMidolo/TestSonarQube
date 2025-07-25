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
    
    # Extract hours, minutes, seconds, and microseconds from the timedelta
    total_seconds = delta.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    microseconds = int((total_seconds - int(total_seconds)) * 1_000_000)
    
    # Create a time object
    time_obj = time(hour=hours, minute=minutes, second=seconds, microsecond=microseconds)
    
    # If a timezone is provided, localize the time
    if tz is not None:
        tz = pytz.timezone(tz)
        time_obj = tz.localize(time_obj)
    
    return time_obj