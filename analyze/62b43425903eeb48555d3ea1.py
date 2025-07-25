def _create_in_regex(self) -> Pattern:
    """
    इन-स्टाइल पैरामीटर रेगुलर एक्सप्रेशन बनाएं।

    रिटर्न करता है इन-स्टाइल पैरामीटर रेगुलर एक्सप्रेशन (:class:`re.Pattern`)।
    """
    # Create regex pattern for matching IN style parameters
    # Format: IN(param1, param2, ...)
    pattern = r'IN\s*\((.*?)\)'
    
    # Compile and return the regex pattern
    return re.compile(pattern, re.IGNORECASE)