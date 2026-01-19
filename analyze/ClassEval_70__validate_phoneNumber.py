def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
    Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
    :param phoneNumber: str, the phone number to validate
    :return: str, the validated phone number or None if invalid
    """
    if not phoneNumber or len(phoneNumber.strip()) == 0:
        return None
    
    # Remove any non-digit characters for validation
    digits_only = ''.join(filter(str.isdigit, phoneNumber))
    
    # Check if it's exactly 11 digits
    if len(digits_only) == 11:
        return phoneNumber
    else:
        return None