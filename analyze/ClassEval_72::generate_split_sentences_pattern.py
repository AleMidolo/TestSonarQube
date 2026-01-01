def generate_split_sentences_pattern(self):
    """
        Generate regular expression pattern that matches the characters between two sentences
        :return: string, regular expression pattern that matches the characters between two sentences
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
        '[.!?][\\s]{1,2}(?=[A-Z])'
        """
    return '[.!?][\\s]{1,2}(?=[A-Z])'