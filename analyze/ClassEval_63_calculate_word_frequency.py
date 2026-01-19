def calculate_word_frequency(self, words_list):
    """
        计算词汇表中每个单词的词频，并按值降序排序词频字典。
        :param words_list: 一个单词列表的列表
        :return: 前5个词频字典，一个词频字典，键是单词，值是频率
        >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    all_words = []
    for words in words_list:
        all_words.extend(words)
    word_counter = Counter(all_words)
    top_5 = dict(word_counter.most_common(5))
    return top_5