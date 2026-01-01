def remove_stop_words(self, string_list, stop_word_list):
    """
        从字符串列表中移除所有停用词。
        :param string_list: 字符串列表
        :param stop_word_list: 停用词列表
        :return: 不包含停用词的单词列表
        >>> NLPDataProcessor().remove_stop_words(['This is a test.'], ['a', 'an', 'the'])
        [['This', 'is', 'test.']]
        """
    processed_list = []
    for string in string_list:
        words = string.split()
        filtered_words = [word for word in words if word.lower() not in stop_word_list]
        processed_list.append(filtered_words)
    return processed_list