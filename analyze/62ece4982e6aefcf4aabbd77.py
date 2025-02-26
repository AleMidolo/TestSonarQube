import datetime
import re

def parse_frequency(frequency):
    """
    Given a frequency string with a number and a unit of time, return a corresponding
    datetime.timedelta instance or None if the frequency is None or "always".

    For instance, given "3 weeks", return datetime.timedelta(weeks=3)

    Raise ValueError if the given frequency cannot be parsed.
    """
    if frequency is None or frequency.lower() == "always":
        return None

    match = re.match(r'(\d+)\s*(seconds?|minutes?|hours?|days?|weeks?|months?|years?)', frequency, re.IGNORECASE)
    if not match:
        raise ValueError(f"Cannot parse frequency: {frequency}")

    value, unit = match.groups()
    value = int(value)

    if unit.lower().startswith('second'):
        return datetime.timedelta(seconds=value)
    elif unit.lower().startswith('minute'):
        return datetime.timedelta(minutes=value)
    elif unit.lower().startswith('hour'):
        return datetime.timedelta(hours=value)
    elif unit.lower().startswith('day'):
        return datetime.timedelta(days=value)
    elif unit.lower().startswith('week'):
        return datetime.timedelta(weeks=value)
    elif unit.lower().startswith('month'):
        # Approximate a month as 30 days
        return datetime.timedelta(days=value * 30)
    elif unit.lower().startswith('year'):
        # Approximate a year as 365 days
        return datetime.timedelta(days=value * 365)

    raise ValueError(f"Cannot parse frequency: {frequency}")