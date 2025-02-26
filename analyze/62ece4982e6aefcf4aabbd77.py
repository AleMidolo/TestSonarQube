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
    
    # Define a regex pattern to match the frequency string
    pattern = r'(\d+)\s*(seconds?|minutes?|hours?|days?|weeks?|months?|years?)'
    match = re.match(pattern, frequency, re.IGNORECASE)
    
    if not match:
        raise ValueError(f"Cannot parse frequency: {frequency}")
    
    value, unit = match.groups()
    value = int(value)
    
    # Map the unit to the corresponding timedelta argument
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
        'month': 'days',  # Approximation: 1 month = 30 days
        'months': 'days',  # Approximation: 1 month = 30 days
        'year': 'days',    # Approximation: 1 year = 365 days
        'years': 'days'    # Approximation: 1 year = 365 days
    }
    
    if unit.lower() in unit_mapping:
        if unit.lower() in ['month', 'months']:
            return datetime.timedelta(days=value * 30)  # Approximation
        elif unit.lower() in ['year', 'years']:
            return datetime.timedelta(days=value * 365)  # Approximation
        else:
            return datetime.timedelta(**{unit_mapping[unit.lower()]: value})
    
    raise ValueError(f"Cannot parse frequency: {frequency}")