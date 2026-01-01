def get_pos_tag(self, sentence):
    """
        वाक्य से पंक्चुएशन हटाएँ और इनपुट वाक्य को टोकनाइज़ करें,
        फिर हर शब्द के लिए पार्ट-ऑफ़-स्पीच (POS) टैग को मार्क करें।

        :param sentence: str, एक वाक्य
        :return: list, वाक्य में हर शब्द के लिए POS टैग

        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("मैं एक रेस में दौड़ रहा हूँ।")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
        """
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    pos_tags = [tag for word, tag in tagged_words]
    return pos_tags