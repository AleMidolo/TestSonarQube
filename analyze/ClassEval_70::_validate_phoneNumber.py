def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
        Validate the phone number and return it. If phoneNumber is empty or not 11 digits, set to None.
        :param phoneNumber: str, the phone number to validate
        :return: str, the validated phone number or None if invalid
        """
    if not phoneNumber or not phoneNumber.isdigit() or len(phoneNumber) != 11:
        return None
    return phoneNumber