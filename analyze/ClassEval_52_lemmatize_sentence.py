def lemmatize_sentence(self, sentence):
    """
        Elimina la puntuación de la oración y tokeniza la oración de entrada, marca la etiqueta de parte del discurso de cada palabra,
        lematiza las palabras con diferentes parámetros basados en sus partes del discurso y las almacena en una lista.
        :param sentence: una cadena de texto que representa una oración
        :return: una lista de palabras que han sido lematizadas.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """
    pos_tags = self.get_pos_tag(sentence)
    words = self.remove_punctuation(sentence).split()
    lemmatized_words = []
    for word, pos in zip(words, pos_tags):
        if pos.startswith('V'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
        elif pos.startswith('N'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='n')
        elif pos.startswith('J'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
        else:
            lemmatized_word = self.lemmatizer.lemmatize(word)
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words