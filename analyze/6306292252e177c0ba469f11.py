from datetime import datetime

def format_dt(dt):
    return ensure_timezone(dt).strftime('%Y-%m-%dT%H:%M:%S%z')