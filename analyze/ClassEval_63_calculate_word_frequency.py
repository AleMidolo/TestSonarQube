def calculate_word_frequency(self, words_list):
    """
    计算词汇表中每个单词的词频，并按值降序排序词频字典。
    :param words_list: 一个单词列表的列表
    :return: 前5个词频字典，一个词频字典，键是单词，值是频率
    >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    word_freq = {}
    
    # Count frequency of each word
    for word_list in words_list:
        for word in word_list:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency (descending) and then by word (for stable ordering)
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: (-x[1], x[0])))
    
    return sorted_word_freq