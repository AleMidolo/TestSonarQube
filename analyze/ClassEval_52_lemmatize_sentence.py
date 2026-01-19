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
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    lemmatized_words = []
    for word, tag in tagged_words:
        wn_tag = self.get_wordnet_pos(tag)
        if wn_tag:
            lemmatized_word = self.lemmatizer.lemmatize(word, wn_tag)
        else:
            lemmatized_word = self.lemmatizer.lemmatize(word)
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words