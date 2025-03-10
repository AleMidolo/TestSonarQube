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
    
    number = int(match.group(1))
    unit = match.group(2).lower()
    
    if unit == "second":
        return timedelta(seconds=number)
    elif unit == "minute":
        return timedelta(minutes=number)
    elif unit == "hour":
        return timedelta(hours=number)
    elif unit == "day":
        return timedelta(days=number)
    elif unit == "week":
        return timedelta(weeks=number)
    elif unit == "month":
        return timedelta(days=number * 30)  # Approximation
    elif unit == "year":
        return timedelta(days=number * 365)  # Approximation
    else:
        raise ValueError(f"Unsupported time unit: {unit}")