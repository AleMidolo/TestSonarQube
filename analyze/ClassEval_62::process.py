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