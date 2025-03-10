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
    
    unit_mapping = {
        "सेकंड": "seconds",
        "मिनट": "minutes",
        "घंटे": "hours",
        "दिन": "days",
        "सप्ताह": "weeks",
    }
    
    if unit not in unit_mapping:
        raise ValueError(f"Unknown time unit: {unit}")
    
    return timedelta(**{unit_mapping[unit]: num})