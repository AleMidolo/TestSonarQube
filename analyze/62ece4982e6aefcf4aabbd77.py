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
    
    try:
        num, unit = frequency.strip().split()
        num = int(num)
    except ValueError:
        raise ValueError("Invalid frequency format")
    
    unit = unit.lower()
    
    if unit == "सेकंड" or unit == "सेकंडों":
        return timedelta(seconds=num)
    elif unit == "मिनट" or unit == "मिनटों":
        return timedelta(minutes=num)
    elif unit == "घंटे" or unit == "घंटों":
        return timedelta(hours=num)
    elif unit == "दिन" or unit == "दिनों":
        return timedelta(days=num)
    elif unit == "सप्ताह" or unit == "सप्ताहों":
        return timedelta(weeks=num)
    elif unit == "महीने" or unit == "महीनों":
        return timedelta(days=num * 30)  # Approximate
    elif unit == "साल" or unit == "सालों":
        return timedelta(days=num * 365)  # Approximate
    else:
        raise ValueError("Unknown time unit")