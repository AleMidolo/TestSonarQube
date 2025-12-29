def process(self, string_list):
    """
        仅保留字符串中的英文字母和空格，然后将字符串转换为小写，再将字符串拆分为单词列表。计算单词列表中每个单词的词频，并按值降序对词频字典进行排序。
        :param string_list: 字符串列表
        :return: 前5个词频字典，词频字典，键是单词，值是频率
        >>> NLPDataProcessor2.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    words_list = self.process_data(string_list)
    return self.calculate_word_frequency(words_list)