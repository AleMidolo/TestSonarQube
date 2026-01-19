def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
    Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
    :param phoneNumber: str, the phone number to validate
    :return: str, the validated phone number or None if invalid
    """
    if not phoneNumber or not phoneNumber.isdigit() or len(phoneNumber) != 11:
        return None
    return phoneNumber