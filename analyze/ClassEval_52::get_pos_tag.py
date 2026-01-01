def get_pos_tag(self, sentence):
    """
        Rimuove la punteggiatura dalla frase e tokenizza la frase di input, contrassegnando il tag della parte del discorso di ogni parola.
        :param sentence: una stringa di frase
        :return: lista, tag della parte del discorso di ogni parola nella frase.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

        """
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    pos_tags = [tag for word, tag in tagged_words]
    return pos_tags