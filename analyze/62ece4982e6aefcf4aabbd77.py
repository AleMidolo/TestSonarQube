import re
from datetime import timedelta

def parse_frequency(frequency):
    if frequency is None or frequency.lower() == "हमेशा":
        return None
    
    pattern = re.compile(r'(\d+)\s*(सप्ताह|दिन|घंटे|मिनट|सेकंड)')
    match = pattern.match(frequency)
    
    if not match:
        raise ValueError("Invalid frequency format")
    
    value = int(match.group(1))
    unit = match.group(2)
    
    if unit == "सप्ताह":
        return timedelta(weeks=value)
    elif unit == "दिन":
        return timedelta(days=value)
    elif unit == "घंटे":
        return timedelta(hours=value)
    elif unit == "मिनट":
        return timedelta(minutes=value)
    elif unit == "सेकंड":
        return timedelta(seconds=value)
    else:
        raise ValueError("Unsupported time unit")