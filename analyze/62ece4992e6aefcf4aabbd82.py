import re

def get_pattern(pattern, strip=True):
    """
    यह मेथड दी गई स्ट्रिंग को रेगुलर एक्सप्रेशन (Regex) पैटर्न में बदलता है।
    """
    if strip:
        pattern = pattern.strip()
    return re.compile(pattern)