import re

def validate_phone_number(self, phone_number):
    """
    Verify if the phone number is valid
    :param phone_number: Phone number to be verified
    :return: True or False, indicating whether the phone number is valid
    >>> ru = RegexUtils()
    >>> ru.validate_phone_number("123-456-7890")
    True
    """
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone_number))