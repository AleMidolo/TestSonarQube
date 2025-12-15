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
    
    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor.remove_stop_words(['This is a test.'], ['a', 'an', 'the'])
        [['This', 'is', 'test.']]
        """
        answer = []
        for string in string_list:
            string_split = string.split()
            for word in string_split[:]:  # Iterate over a copy of the list
                if word in stop_word_list:
                    string_split.remove(word)
            answer.append(string_split)
        return answer
    
    @classmethod
    def process(cls, string_list):
        """
        构建一个包含 'a', 'an', 'the' 的停用词列表，并从字符串列表中移除所有停用词。
        :param string_list: 字符串列表
        :return: 不包含停用词的单词列表
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        stop_word_list = cls.construct_stop_word_list(cls)
        return cls.remove_stop_words(cls, string_list, stop_word_list)