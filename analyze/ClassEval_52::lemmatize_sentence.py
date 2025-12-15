def lemmatize_sentence(self, sentence):
    """
    Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
    lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
    :param sentence: a sentence str
    :return: a list of words which have been lemmatized.
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