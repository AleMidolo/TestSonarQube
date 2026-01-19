def validate_phone_number(self, phone_number):
    """
        Verify if the phone number is valid
        :param phone_number: Phone number to be verified
        :return: True or False, indicating whether the phone number is valid
        >>> ru = RegexUtils()
        >>> ru.validate_phone_number("123-456-7890")
        True
        """
    pattern = self.generate_phone_number_pattern()
    return self.match(pattern, phone_number)