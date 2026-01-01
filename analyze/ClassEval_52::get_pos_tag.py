def get_pos_tag(self, sentence):
    """
        Removes punctuation from the input text and tokenizes the input sentence, marking the part of speech tag for each word.
        :param sentence: a sentence str
        :return: list, part of speech tags for each word in the sentence.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
        """
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    return [tag for word, tag in tagged_words]