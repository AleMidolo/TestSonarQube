def count_words(self, sentence):
    """
    计算句子中的单词数量。注意，单词由空格分隔，标点符号和数字不算作单词。
    :param sentence:字符串, 要计算的句子，单词由空格分隔
    :return:int, 句子中的单词数量
    >>> ss.count_words("abc def")
    2
    """
    import re
    
    # 按空格分隔句子
    words = sentence.split()
    
    # 计数只包含字母的单词
    count = 0
    for word in words:
        # 移除标点符号后检查是否只包含字母
        cleaned_word = re.sub(r'[^a-zA-Z]', '', word)
        if cleaned_word:  # 如果清理后还有字母，则计数
            count += 1
    
    return count