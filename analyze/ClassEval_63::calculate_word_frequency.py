def calculate_word_frequency(self, words_list):
    """
        计算词汇表中每个单词的词频，并按值降序排序词频字典。
        :param words_list: 一个单词列表的列表
        :return: 前5个词频字典，一个词频字典，键是单词，值是频率
        >>> NLPDataProcessor2.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    flat_list = [word for sublist in words_list for word in sublist]
    word_count = Counter(flat_list)
    return dict(word_count.most_common(5))