from datetime import timedelta

def parse_frequency(frequency):
    if frequency is None or frequency.lower() == "always":
        return None
    
    try:
        parts = frequency.strip().split()
        if len(parts) != 2:
            raise ValueError("Invalid frequency format. Expected format: 'number timeunit'")
        
        num = int(parts[0])
        unit = parts[1].lower()
        
        if unit in ['days', 'day']:
            return timedelta(days=num)
        elif unit in ['weeks', 'week']:
            return timedelta(weeks=num)
        elif unit in ['hours', 'hour']:
            return timedelta(hours=num)
        elif unit in ['minutes', 'minute']:
            return timedelta(minutes=num)
        elif unit in ['seconds', 'second']:
            return timedelta(seconds=num)
        else:
            raise ValueError(f"Unsupported time unit: {unit}")
    
    except ValueError as e:
        raise ValueError(f"Failed to parse frequency: {frequency}. Error: {e}")