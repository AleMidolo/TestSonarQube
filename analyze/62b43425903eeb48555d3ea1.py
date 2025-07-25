import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    इन-स्टाइल पैरामीटर रेगुलर एक्सप्रेशन बनाएं।

    रिटर्न करता है इन-स्टाइल पैरामीटर रेगुलर एक्सप्रेशन (:class:`re.Pattern`)।
    """
    # Example regex pattern for in-style parameters
    pattern = r'\b(?:in|IN)\s+([a-zA-Z_][a-zA-Z0-9_]*)\b'
    return re.compile(pattern)