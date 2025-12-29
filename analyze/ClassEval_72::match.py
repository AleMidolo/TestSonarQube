def match(self, pattern, text):
    """
        Check if the text matches the regular expression
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: True or False, indicating whether the text matches the regular expression
        >>> ru = RegexUtils()
        >>> ru.match(r'\x08\\d{3}-\\d{3}-\\d{4}\x08', "123-456-7890")
        True
        """
    return bool(re.match(pattern, text))