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

    time_units = {
        'सेकंड': 'seconds',
        'मिनट': 'minutes',
        'घंटा': 'hours',
        'दिन': 'days',
        'सप्ताह': 'weeks',
        'महीना': 'months',
        'साल': 'years'
    }

    match = re.match(r'(\d+)\s*([^\s]+)', frequency)
    if not match:
        raise ValueError("Invalid frequency format")

    value, unit = match.groups()
    value = int(value)

    if unit not in time_units:
        raise ValueError("Invalid time unit")

    if unit == 'महीना':
        return timedelta(days=value * 30)  # Approximation
    elif unit == 'साल':
        return timedelta(days=value * 365)  # Approximation

    return timedelta(**{time_units[unit]: value})