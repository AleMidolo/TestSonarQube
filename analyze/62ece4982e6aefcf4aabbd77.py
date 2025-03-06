import re
from datetime import timedelta

def parse_frequency(frequency):
    """
    Given a frequency string with a number and a unit of time, return a corresponding
    datetime.timedelta instance or None if the frequency is None or "always".

    For instance, given "3 weeks", return datetime.timedelta(weeks=3)

    Raise ValueError if the given frequency cannot be parsed.
    """
    if frequency is None or frequency.lower() == "always":
        return None
    
    pattern = re.compile(r'^(\d+)\s*(second|minute|hour|day|week|month|year)s?$', re.IGNORECASE)
    match = pattern.match(frequency.strip())
    
    if not match:
        raise ValueError(f"Invalid frequency format: {frequency}")
    
    value = int(match.group(1))
    unit = match.group(2).lower()
    
    if unit == "second":
        return timedelta(seconds=value)
    elif unit == "minute":
        return timedelta(minutes=value)
    elif unit == "hour":
        return timedelta(hours=value)
    elif unit == "day":
        return timedelta(days=value)
    elif unit == "week":
        return timedelta(weeks=value)
    elif unit == "month":
        return timedelta(days=value * 30)  # Approximation
    elif unit == "year":
        return timedelta(days=value * 365)  # Approximation
    else:
        raise ValueError(f"Unsupported time unit: {unit}")