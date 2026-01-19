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
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    lemmatized_words = []
    for word, tag in tagged_words:
        if tag.startswith('V'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
        elif tag.startswith('J'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
        elif tag.startswith('R'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='r')
        elif tag.startswith('N'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='n')
        else:
            lemmatized_word = self.lemmatizer.lemmatize(word)
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words