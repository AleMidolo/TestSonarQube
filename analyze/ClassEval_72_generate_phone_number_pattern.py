def generate_phone_number_pattern(self):
    """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\x08\\d{3}-\\d{3}-\\d{4}\x08'
        """
    pattern = '\\b\\d{3}-\\d{3}-\\d{4}\\b'
    return pattern