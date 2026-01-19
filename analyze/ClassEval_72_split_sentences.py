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
    sentences = re.split(pattern, text)
    result = []
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            result.append(sentence.rstrip('.!?'))
        else:
            result.append(sentence)
    return result