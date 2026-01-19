def get_pos_tag(self, sentence):
    """
    移除句子中的标点符号并对输入句子进行分词，为每个单词标记词性标签。
    :param sentence: 一个句子，str
    :return: list，句子中每个单词的词性标签。
    >>> lemmatization = Lemmatization()
    >>> lemmatization.get_pos_tag("I am running in a race.")
    ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
    """
    import string
    import nltk
    
    # 移除标点符号
    translator = str.maketrans('', '', string.punctuation)
    sentence_no_punct = sentence.translate(translator)
    
    # 分词
    words = sentence_no_punct.split()
    
    # 词性标注
    pos_tags = nltk.pos_tag(words)
    
    # 只返回词性标签
    return [tag for word, tag in pos_tags]