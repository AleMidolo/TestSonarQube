from datetime import datetime, timedelta, timezone

def hydrate_time(nanoseconds, tz=None):
    seconds = nanoseconds / 1_000_000_000
    time_delta = timedelta(seconds=seconds)
    base_time = datetime(1970, 1, 1, tzinfo=timezone.utc) + time_delta
    
    if tz:
        local_time = base_time.astimezone(tz)
        return local_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    return base_time.strftime('%Y-%m-%d %H:%M:%S UTC')