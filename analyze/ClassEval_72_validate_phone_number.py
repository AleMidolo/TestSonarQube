def validate_phone_number(self, phone_number):
    """
    फोन नंबर की वैधता की पुष्टि करें
    :param phone_number: पुष्टि करने के लिए फोन नंबर
    :return: True या False, यह दर्शाते हुए कि फोन नंबर वैध है या नहीं
    >>> ru = RegexUtils()
    >>> ru.validate_phone_number("123-456-7890")
    True
    """
    import re
    
    # Pattern for phone numbers in format: XXX-XXX-XXXX
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    
    if re.match(pattern, phone_number):
        return True
    return False