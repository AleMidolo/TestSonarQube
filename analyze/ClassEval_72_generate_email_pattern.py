def generate_email_pattern(self):
    """
        Generate regular expressions that match email addresses
        :return: string, regular expressions that match email addresses
        >>> ru = RegexUtils()
        >>> ru.generate_email_pattern()
        '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
        """
    pattern = '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
    return pattern