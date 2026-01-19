def process(self, string_list):
    """
    仅保留字符串中的英文字母和空格,然后将字符串转换为小写,再将字符串拆分为单词列表。计算单词列表中每个单词的词频,并按值降序对词频字典进行排序。
    :param string_list: 字符串列表
    :return: 前5个词频字典,词频字典,键是单词,值是频率
    >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    word_freq = {}
    
    for string in string_list:
        # 仅保留英文字母和空格
        cleaned = ''.join(char if char.isalpha() or char.isspace() else '' for char in string)
        # 转换为小写
        cleaned = cleaned.lower()
        # 拆分为单词列表
        words = cleaned.split()
        
        # 计算词频
        for word in words:
            if word:  # 确保不是空字符串
                word_freq[word] = word_freq.get(word, 0) + 1
    
    # 按值降序排序
    sorted_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    
    # 返回前5个
    top_5 = dict(list(sorted_freq.items())[:5])
    
    return top_5