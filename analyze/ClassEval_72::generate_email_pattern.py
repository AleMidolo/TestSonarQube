def generate_email_pattern(self):
    """
        Genera espressioni regolari che corrispondono agli indirizzi email
        :return: stringa, espressioni regolari che corrispondono agli indirizzi email
        >>> ru = RegexUtils()
        >>> ru.generate_email_pattern()
        '\x08[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\x08'
        """
    pattern = '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
    return pattern