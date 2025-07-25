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
        raise ValueError("Invalid time unit")