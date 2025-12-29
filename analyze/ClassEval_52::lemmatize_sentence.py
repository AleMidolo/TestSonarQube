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
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    lemmatized_words = []
    for word, tag in tagged_words:
        if tag.startswith('J'):
            pos = 'a'
        elif tag.startswith('V'):
            pos = 'v'
        elif tag.startswith('N'):
            pos = 'n'
        elif tag.startswith('R'):
            pos = 'r'
        else:
            pos = 'n'
        lemmatized_word = self.lemmatizer.lemmatize(word, pos=pos)
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words