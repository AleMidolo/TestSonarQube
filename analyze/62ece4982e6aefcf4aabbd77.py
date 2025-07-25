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
        units = {
            'days': 'days',
            'day': 'days',
            'd': 'days',
            'weeks': 'weeks', 
            'week': 'weeks',
            'w': 'weeks',
            'hours': 'hours',
            'hour': 'hours', 
            'h': 'hours',
            'minutes': 'minutes',
            'minute': 'minutes',
            'min': 'minutes',
            'm': 'minutes',
            'seconds': 'seconds',
            'second': 'seconds',
            'sec': 'seconds',
            's': 'seconds',
            'microseconds': 'microseconds',
            'microsecond': 'microseconds',
            'us': 'microseconds'
        }
        
        if unit not in units:
            raise ValueError(f"Invalid time unit: {unit}")
            
        # Create timedelta with the appropriate unit
        kwargs = {units[unit]: number}
        return timedelta(**kwargs)
        
    except ValueError as e:
        raise ValueError(f"Failed to parse frequency '{frequency}': {str(e)}")