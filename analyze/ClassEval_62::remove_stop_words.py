class NLPDataProcessor: 

    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        >>> NLPDataProcessor.construct_stop_word_list()
        ['a', 'an', 'the']
        """
        stop_word_list = ['a', 'an', 'the']
        return stop_word_list
    
    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        stop_word_list = self.construct_stop_word_list()
        words_list = self.remove_stop_words(string_list, stop_word_list)
        return words_list
    
    def remove_stop_words(self, string_list, stop_word_list):
        """
        从字符串列表中移除所有停用词。
        :param string_list: 字符串列表
        :param stop_word_list: 停用词列表
        :return: 不包含停用词的单词列表
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        words_list = []
        for string in string_list:
            words = string.split()
            filtered_words = [word for word in words if word.lower() not in stop_word_list]
            words_list.append(filtered_words)
        return words_list