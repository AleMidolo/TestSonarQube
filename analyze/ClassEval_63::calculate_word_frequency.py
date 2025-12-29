def calculate_word_frequency(self, words_list):
    """
        计算词汇表中每个单词的词频，并按值降序排序词频字典。
        :param words_list: 一个单词列表的列表
        :return: 前5个词频字典，一个词频字典，键是单词，值是频率
        >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    word_counter = Counter()
    for words in words_list:
        word_counter.update(words)
    sorted_items = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
    top_5_items = sorted_items[:5]
    top_5_dict = dict(top_5_items)
    return top_5_dict