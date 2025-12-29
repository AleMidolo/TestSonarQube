def lemmatize_sentence(self, sentence):
    """
    पंक्चुएशन हटाता है और इनपुट सेंटेंस को टोकनाइज़ करता है।
    हर शब्द को पार्ट-ऑफ़-स्पीच टैग से मार्क करता है।
    फिर उनके पार्ट-ऑफ़-स्पीच के आधार पर अलग-अलग पैरामीटर के साथ लेमेटाइज़ करता है,
    और उन्हें एक लिस्ट में स्टोर करता है।

    :param sentence: str, एक इनपुट सेंटेंस
    :return: list, लेमेटाइज़ किए गए शब्दों की लिस्ट

    >>> lemmatization = Lemmatization()
    >>> lemmatization.lemmatize_sentence("I am running in a race.")
    ['I', 'to be', 'running', 'in', 'a', 'race']
    """
    pos_tags = self.get_pos_tag(sentence)
    words = self.remove_punctuation(sentence).split()
    lemmatized_words = []
    for word, pos in zip(words, pos_tags):
        if pos.startswith('VB'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
        elif pos.startswith('NN'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='n')
        elif pos.startswith('JJ'):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
        else:
            lemmatized_word = word
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words