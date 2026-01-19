def process_data(self, string_list):
    """
    仅保留字符串中的英文字母和空格，然后将字符串转换为小写，再将字符串拆分为单词列表。
    :param string_list: 字符串列表
    :return: words_list: 单词列表的列表
    >>> NLPDataProcessor.process_data(['This is a test.'])
    [['this', 'is', 'a', 'test']]
    """
    words_list = []
    for string in string_list:
        # 仅保留英文字母和空格
        filtered_string = ''.join(char if char.isalpha() or char.isspace() else '' for char in string)
        # 转换为小写
        lowercase_string = filtered_string.lower()
        # 拆分为单词列表
        words = lowercase_string.split()
        words_list.append(words)
    return words_list