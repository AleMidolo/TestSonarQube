import re

def _create_in_regex(self) -> Pattern:
    """
    इन-स्टाइल पैरामीटर रेगुलर एक्सप्रेशन बनाएं।

    रिटर्न करता है इन-स्टाइल पैरामीटर रेगुलर एक्सप्रेशन (:class:`re.Pattern`)।
    """
    return re.compile(r'\{([^}]+)\}')