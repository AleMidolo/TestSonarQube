def parse_frequency(frequency):
    import datetime
    import re

    if frequency is None or frequency.lower() == "always":
        return None

    # Regular expression to match number and unit
    match = re.match(r"(\d+)\s*(\w+)", frequency.strip())
    if not match:
        raise ValueError(f"Invalid frequency format: {frequency}")

    value = int(match.group(1))
    unit = match.group(2).lower()

    # Map of units to timedelta arguments
    units_map = {
        'second': 'seconds',
        'seconds': 'seconds',
        'sec': 'seconds',
        'secs': 'seconds',
        'minute': 'minutes', 
        'minutes': 'minutes',
        'min': 'minutes',
        'mins': 'minutes',
        'hour': 'hours',
        'hours': 'hours',
        'hr': 'hours',
        'hrs': 'hours',
        'day': 'days',
        'days': 'days',
        'week': 'weeks',
        'weeks': 'weeks',
    }

    if unit not in units_map:
        raise ValueError(f"Invalid time unit: {unit}")

    # Create timedelta with the appropriate unit
    kwargs = {units_map[unit]: value}
    return datetime.timedelta(**kwargs)