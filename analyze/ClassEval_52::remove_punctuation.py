def remove_punctuation(self, sentence):
    """
        Elimina la puntuación del texto de entrada.
        :param sentence: una cadena de texto
        :return: str, cadena sin ninguna puntuación
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """
    translator = str.maketrans('', '', string.punctuation)
    return sentence.translate(translator)