def parse_frequency(frequency):
    import datetime
    import re
    
    if frequency is None or frequency.lower() == "हमेशा":
        return None
        
    # Match number and unit pattern
    match = re.match(r"(\d+)\s*([^\d\s]+)", frequency)
    if not match:
        raise ValueError(f"Invalid frequency format: {frequency}")
        
    number = int(match.group(1))
    unit = match.group(2).strip().lower()
    
    # Map Hindi units to timedelta arguments
    unit_map = {
        'दिन': 'days',
        'दिनों': 'days',
        'सप्ताह': 'weeks', 
        'हफ्ता': 'weeks',
        'हफ्ते': 'weeks',
        'महीना': 'days',
        'महीने': 'days',
        'साल': 'days',
        'वर्ष': 'days'
    }
    
    if unit not in unit_map:
        raise ValueError(f"Invalid time unit: {unit}")
        
    # Convert months/years to days
    if unit in ['महीना', 'महीने']:
        number *= 30
    elif unit in ['साल', 'वर्ष']:
        number *= 365
        
    # Create timedelta with appropriate argument
    kwargs = {unit_map[unit]: number}
    return datetime.timedelta(**kwargs)