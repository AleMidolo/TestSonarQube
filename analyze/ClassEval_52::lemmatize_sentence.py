def lemmatize_sentence(self, sentence):
    """
        Rimuove la punteggiatura dalla frase e tokenizza la frase di input, contrassegna il tag della parte del discorso di ogni parola,
        lemmatizza le parole con parametri diversi in base alle loro parti del discorso e le memorizza in una lista.
        :param sentence: una stringa di frase
        :return: una lista di parole che sono state lemmatizzate.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """
    pos_tags = self.get_pos_tag(sentence)
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
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