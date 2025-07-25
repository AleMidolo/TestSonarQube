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
    unit_mapping = {
        'दिन': 'days',
        'दिनों': 'days',
        'सप्ताह': 'weeks', 
        'हफ्ता': 'weeks',
        'हफ्ते': 'weeks',
        'महीना': 'days',
        'महीने': 'days',
        'साल': 'days',
        'वर्ष': 'days',
        'घंटा': 'hours',
        'घंटे': 'hours',
        'मिनट': 'minutes',
        'सेकंड': 'seconds'
    }
    
    if unit not in unit_mapping:
        raise ValueError(f"Invalid time unit: {unit}")
        
    # Handle special cases for months and years
    if unit in ['महीना', 'महीने']:
        return datetime.timedelta(days=number * 30)
    elif unit in ['साल', 'वर्ष']:
        return datetime.timedelta(days=number * 365)
    else:
        # Create timedelta with mapped unit
        return datetime.timedelta(**{unit_mapping[unit]: number})