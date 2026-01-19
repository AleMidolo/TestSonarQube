def process(self, string_list):
    """
    构建一个包含 'a', 'an', 'the' 的停用词列表，并从字符串列表中移除所有停用词。
    :param string_list: 字符串列表
    :return: 不包含停用词的单词列表
    >>> NLPDataProcessor.process(['This is a test.'])
    [['This', 'is', 'test.']]
    """
    stop_words = ['a', 'an', 'the']
    result = []

    for string in string_list:
        words = string.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        result.append(filtered_words)

    return result