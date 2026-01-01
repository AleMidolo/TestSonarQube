def split_sentences(self, text):
    """
        Split the text into a list of sentences without Punctuation except the last sentence
        :param text: Text to be split
        :return: Split Text List
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """
    pattern = self.generate_split_sentences_pattern()
    parts = re.split(pattern, text)
    result = []
    for i, part in enumerate(parts):
        if i < len(parts) - 1:
            result.append(part.rstrip('.!?'))
        else:
            result.append(part)
    return result