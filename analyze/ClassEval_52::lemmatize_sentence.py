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
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    lemmatized_words = []
    for word, tag in tagged_words:
        if tag.startswith('V'):
            if word.lower() == 'am' or word.lower() == 'is' or word.lower() == 'are':
                lemmatized_words.append('to be')
            else:
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='v'))
        elif tag.startswith('J'):
            lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='a'))
        elif tag.startswith('R'):
            lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='r'))
        else:
            lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='n'))
    return lemmatized_words