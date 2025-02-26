import datetime

def parse_frequency(frequency):
    """
    Given a frequency string with a number and a unit of time, return a corresponding
    datetime.timedelta instance or None if the frequency is None or "always".

    For instance, given "3 weeks", return datetime.timedelta(weeks=3)

    Raise ValueError if the given frequency cannot be parsed.
    """
    if frequency is None or frequency.lower() == "always":
        return None

    units = {
        'seconds': 'seconds',
        'second': 'seconds',
        'minutes': 'minutes',
        'minute': 'minutes',
        'hours': 'hours',
        'hour': 'hours',
        'days': 'days',
        'day': 'days',
        'weeks': 'weeks',
        'week': 'weeks',
        'months': 'days',  # Approximation: 1 month = 30 days
        'month': 'days',    # Approximation: 1 month = 30 days
        'years': 'days',    # Approximation: 1 year = 365 days
        'year': 'days'      # Approximation: 1 year = 365 days
    }

    parts = frequency.split()
    if len(parts) != 2:
        raise ValueError(f"Cannot parse frequency: {frequency}")

    try:
        value = int(parts[0])
    except ValueError:
        raise ValueError(f"Cannot parse frequency value: {parts[0]}")

    unit = parts[1].lower()
    if unit not in units:
        raise ValueError(f"Cannot parse frequency unit: {unit}")

    return datetime.timedelta(**{units[unit]: value})