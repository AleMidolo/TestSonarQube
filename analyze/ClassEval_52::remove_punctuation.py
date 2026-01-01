def remove_punctuation(self, sentence):
    """
        Rimuove la punteggiatura dal testo di input.
        :param sentence: una frase str
        :return: str, frase senza alcuna punteggiatura
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """
    translator = str.maketrans('', '', string.punctuation)
    return sentence.translate(translator)