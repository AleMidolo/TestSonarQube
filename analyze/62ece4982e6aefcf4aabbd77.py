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
        'second': 'seconds',
        'minute': 'minutes',
        'hour': 'hours',
        'day': 'days',
        'week': 'weeks',
        'month': 'days',  # Approximation: 1 month = 30 days
        'year': 'days'    # Approximation: 1 year = 365 days
    }
    
    if unit.lower() in unit_mapping:
        if unit.lower() in ['month', 'year']:
            if unit.lower() == 'month':
                return datetime.timedelta(days=value * 30)
            else:
                return datetime.timedelta(days=value * 365)
        return datetime.timedelta(**{unit_mapping[unit.lower()]: value})
    
    raise ValueError(f"Cannot parse frequency: {frequency}")