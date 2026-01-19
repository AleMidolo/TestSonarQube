def lemmatize_sentence(self, sentence):
    """
    移除句子中的标点符号并对输入句子进行分词,为每个单词标记词性标签,
    根据它们的词性对单词进行词形还原,并将结果存储在一个列表中。
    :param sentence: 一个句子,str
    :return: 一个已进行词形还原的单词列表。
    >>> lemmatization = Lemmatization()
    >>> lemmatization.lemmatize_sentence("I am running in a race.")
    ['I', 'be', 'run', 'in', 'a', 'race']
    """
    import string
    import nltk
    from nltk import word_tokenize, pos_tag
    from nltk.corpus import wordnet
    from nltk.stem import WordNetLemmatizer
    
    # 移除标点符号
    translator = str.maketrans('', '', string.punctuation)
    sentence_no_punct = sentence.translate(translator)
    
    # 分词
    tokens = word_tokenize(sentence_no_punct)
    
    # 词性标注
    pos_tags = pos_tag(tokens)
    
    # 初始化词形还原器
    lemmatizer = WordNetLemmatizer()
    
    # 将Penn Treebank标签转换为WordNet标签的辅助函数
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # 默认为名词
    
    # 对每个单词进行词形还原
    lemmatized_words = []
    for word, pos in pos_tags:
        wordnet_pos = get_wordnet_pos(pos)
        lemmatized_word = lemmatizer.lemmatize(word, pos=wordnet_pos)
        lemmatized_words.append(lemmatized_word)
    
    return lemmatized_words