import re
from datetime import timedelta

def parse_frequency(frequency):
    """
    एक संख्या और समय की इकाई के साथ एक आवृत्ति स्ट्रिंग दी गई है, एक संगत
    datetime.timedelta इंस्टेंस लौटाएँ या यदि आवृत्ति None या "हमेशा" है, तो None लौटाएँ।

    उदाहरण के लिए, "3 सप्ताह" दिया गया है, datetime.timedelta(weeks=3) लौटाएँ

    यदि दी गई आवृत्ति को पार्स नहीं किया जा सकता है, तो ValueError उठाएँ।
    """
    if frequency is None or frequency.lower() == "हमेशा":
        return None

    match = re.match(r'(\d+)\s*(\w+)', frequency)
    if not match:
        raise ValueError("Invalid frequency format")

    value, unit = match.groups()
    value = int(value)

    if unit in ['सेकंड', 'सेकंड', 'seconds']:
        return timedelta(seconds=value)
    elif unit in ['मिनट', 'मिनट', 'minutes']:
        return timedelta(minutes=value)
    elif unit in ['घंटा', 'घंटे', 'hours']:
        return timedelta(hours=value)
    elif unit in ['दिन', 'दिन', 'days']:
        return timedelta(days=value)
    elif unit in ['सप्ताह', 'सप्ताह', 'weeks']:
        return timedelta(weeks=value)
    elif unit in ['महीना', 'महीने', 'months']:
        return timedelta(days=value * 30)  # Approximation
    elif unit in ['साल', 'साल', 'years']:
        return timedelta(days=value * 365)  # Approximation
    else:
        raise ValueError("Unknown time unit")