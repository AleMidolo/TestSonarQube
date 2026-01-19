def get_pos_tag(self, sentence):
    """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

        """
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    return [tag for word, tag in tagged_words]