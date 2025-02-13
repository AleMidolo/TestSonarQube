import datetime

def parse_frequency(frequency):
    if frequency is None or frequency.lower() == "always":
        return None
    
    try:
        number, unit = frequency.split()
        number = int(number)
        
        if unit not in ['days', 'seconds', 'microseconds', 'milliseconds', 'minutes', 'hours', 'weeks']:
            raise ValueError("Invalid time unit")
        
        return datetime.timedelta(**{unit: number})
    
    except (ValueError, TypeError):
        raise ValueError("Frequency cannot be parsed")