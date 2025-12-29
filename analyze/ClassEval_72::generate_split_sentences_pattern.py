def generate_split_sentences_pattern(self):
    """
        Generate regular expression patterns that match the central characters of two sentences
        :return: string, regular expression patterns that match the central characters of two sentences
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
        '[.!?][\\s]{1,2}(?=[A-Z])'
        """
    return '[.!?][\\s]{1,2}(?=[A-Z])'