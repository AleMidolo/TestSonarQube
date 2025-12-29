def split(self, pattern, text):
    """
        Split the text based on the regular expression pattern and return a list of substrings
        :param pattern: string, Regular expression pattern
        :param text: string, Text to split
        :return: list of string, List of substrings after splitting
        >>> ru = RegexUtils()
        >>> ru.split(r'\x08\\d{3}-\\d{3}-\\d{4}\x08', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        ['', ' abiguygusu ', ' kjgufwycs ', '']
        """
    return re.split(pattern, text)