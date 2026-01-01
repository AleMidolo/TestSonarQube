def lemmatize_sentence(self, sentence):
    """
        移除句子中的标点符号并对输入句子进行分词，为每个单词标记词性标签，
        根据它们的词性对单词进行词形还原，并将结果存储在一个列表中。
        :param sentence: 一个句子，str
        :return: 一个已进行词形还原的单词列表。
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """
    sentence_no_punct = self.remove_punctuation(sentence)
    words = word_tokenize(sentence_no_punct)
    tagged_words = pos_tag(words)
    lemmatized_words = []
    for word, tag in tagged_words:
        wordnet_tag = self.get_wordnet_pos(tag)
        if wordnet_tag:
            lemmatized_word = self.lemmatizer.lemmatize(word, wordnet_tag)
        else:
            lemmatized_word = self.lemmatizer.lemmatize(word)
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words