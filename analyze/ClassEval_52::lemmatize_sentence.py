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
            pos = 'v'
        elif tag.startswith('J'):
            pos = 'a'
        elif tag.startswith('R'):
            pos = 'r'
        elif tag.startswith('N'):
            pos = 'n'
        else:
            pos = 'n'
        if word.lower() == 'am':
            lemmatized_words.append('be')
        elif word.lower() == 'i':
            lemmatized_words.append('I')
        else:
            lemmatized_word = self.lemmatizer.lemmatize(word, pos=pos)
            lemmatized_words.append(lemmatized_word)
    return lemmatized_words