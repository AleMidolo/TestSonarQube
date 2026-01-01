def get_pos_tag(self, sentence):
    """
        Elimina la puntuación de la oración y tokeniza la oración de entrada, marcando la etiqueta de la parte del discurso de cada palabra.
        :param sentence: una oración str
        :return: lista, etiqueta de la parte del discurso de cada palabra en la oración.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

        """
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    pos_tags = [tag for word, tag in tagged_words]
    return pos_tags