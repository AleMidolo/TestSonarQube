def parse_frequency(frequency):
    """
    Given a frequency string with a number and a unit of time, return a corresponding
    datetime.timedelta instance or None if the frequency is None or "always".

    For instance, given "3 weeks", return datetime.timedelta(weeks=3)

    Raise ValueError if the given frequency cannot be parsed.
    """
    from datetime import timedelta
    
    if frequency is None or frequency.lower() == "always":
        return None
        
    try:
        # Split into number and unit
        parts = frequency.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Invalid frequency format: {frequency}")
            
        number = float(parts[0])
        unit = parts[1].lower().rstrip('s')  # Remove potential plural 's'
        
        # Map units to timedelta parameters
        unit_mapping = {
            'day': 'days',
            'week': 'weeks', 
            'hour': 'hours',
            'minute': 'minutes',
            'second': 'seconds',
            'microsecond': 'microseconds',
            'millisecond': 'milliseconds'
        }
        
        if unit not in unit_mapping:
            raise ValueError(f"Invalid time unit: {unit}")
            
        # Create timedelta with the appropriate unit
        kwargs = {unit_mapping[unit]: number}
        return timedelta(**kwargs)
        
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Could not parse frequency: {frequency}") from e