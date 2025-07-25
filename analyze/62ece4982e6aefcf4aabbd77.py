from datetime import timedelta

def parse_frequency(frequency):
    if frequency is None or frequency == "always":
        return None
        
    try:
        # Split frequency string into number and unit
        parts = frequency.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid frequency format: {frequency}")
            
        number = float(parts[0])
        unit = parts[1].lower()
        
        # Map of valid time units to timedelta parameters
        valid_units = {
            'days': 'days',
            'day': 'days',
            'weeks': 'weeks', 
            'week': 'weeks',
            'hours': 'hours',
            'hour': 'hours',
            'minutes': 'minutes',
            'minute': 'minutes',
            'seconds': 'seconds',
            'second': 'seconds',
            'microseconds': 'microseconds',
            'microsecond': 'microseconds'
        }
        
        if unit not in valid_units:
            raise ValueError(f"Invalid time unit: {unit}")
            
        # Create timedelta with the appropriate unit
        kwargs = {valid_units[unit]: number}
        return timedelta(**kwargs)
        
    except ValueError as e:
        if str(e).startswith("Invalid"):
            raise
        raise ValueError(f"Invalid frequency format: {frequency}")