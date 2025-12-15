def remove_punctuation(self, sentence):
    """
    Remove punctuation from the input text.
    :param sentence: a sentence str
    :return: str, the sentence with all punctuation removed
    >>> lemmatization = Lemmatization()
    >>> lemmatization.remove_punctuation("I am running in a race.")
    'I am running in a race'
    """
    return sentence.translate(str.maketrans('', '', string.punctuation))