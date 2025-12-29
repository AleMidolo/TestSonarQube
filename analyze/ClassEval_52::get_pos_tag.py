def get_pos_tag(self, sentence):
    """
        移除句子中的标点符号并对输入句子进行分词，为每个单词标记词性标签。
        :param sentence: 一个句子，str
        :return: list，句子中每个单词的词性标签。
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
        """
    sentence_no_punct = self.remove_punctuation(sentence)
    words = word_tokenize(sentence_no_punct)
    tagged_words = pos_tag(words)
    pos_tags = [tag for word, tag in tagged_words]
    return pos_tags