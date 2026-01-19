def remove_punctuation(self, sentence):
    """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """
    translator = str.maketrans('', '', string.punctuation)
    return sentence.translate(translator)