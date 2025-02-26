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
    
    # Define regex pattern for matching frequency strings
    pattern = r'(\d+)\s*(seconds?|minutes?|hours?|days?|weeks?|months?|years?)'
    match = re.match(pattern, frequency, re.IGNORECASE)
    
    if not match:
        raise ValueError(f"Cannot parse frequency: {frequency}")
    
    value, unit = match.groups()
    value = int(value)
    
    # Map units to timedelta arguments
    unit_mapping = {
        'second': 'seconds',
        'seconds': 'seconds',
        'minute': 'minutes',
        'minutes': 'minutes',
        'hour': 'hours',
        'hours': 'hours',
        'day': 'days',
        'days': 'days',
        'week': 'weeks',
        'weeks': 'weeks',
        'month': 'days',  # Approximation, as timedelta does not support months
        'months': 'days',  # Approximation
        'year': 'days',    # Approximation
        'years': 'days'    # Approximation
    }
    
    if unit.lower() in unit_mapping:
        if unit.lower() in ['month', 'months']:
            # Assuming 30 days for a month
            return datetime.timedelta(days=value * 30)
        elif unit.lower() in ['year', 'years']:
            # Assuming 365 days for a year
            return datetime.timedelta(days=value * 365)
        else:
            return datetime.timedelta(**{unit_mapping[unit.lower()]: value})
    
    raise ValueError(f"Cannot parse frequency: {frequency}")