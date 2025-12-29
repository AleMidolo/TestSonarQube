def remove_punctuation(self, sentence):
    """
        Rimuove la punteggiatura dal testo di input.
        :param sentence: una frase str
        :return: str, frase senza alcuna punteggiatura
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """
    return sentence.translate(str.maketrans('', '', string.punctuation))