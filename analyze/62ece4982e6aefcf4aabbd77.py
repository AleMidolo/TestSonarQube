def parse_frequency(frequency):
    from datetime import timedelta
    
    if frequency is None or frequency.lower() == "always":
        return None
        
    try:
        # Split into number and unit
        parts = frequency.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Invalid frequency format: {frequency}")
            
        number = float(parts[0])
        unit = parts[1].lower()
        
        # Map units to timedelta parameters
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
            'weeks': 'weeks'
        }
        
        if unit not in unit_mapping:
            raise ValueError(f"Invalid time unit: {unit}")
            
        # Create timedelta with the appropriate parameter
        kwargs = {unit_mapping[unit]: number}
        return timedelta(**kwargs)
        
    except (ValueError, TypeError) as e:
        raise ValueError(f"Could not parse frequency: {frequency}") from e