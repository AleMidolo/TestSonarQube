def count_words(self, sentence):
    """
    计算句子中的单词数量。注意，单词由空格分隔，标点符号和数字不算作单词。
    :param sentence:字符串, 要计算的句子，单词由空格分隔
    :return:int, 句子中的单词数量
    >>> ss.count_words("abc def")
    2
    """
    if not sentence:
        return 0
    
    words = sentence.split()
    count = 0
    
    for word in words:
        # 检查单词是否只包含字母
        if word.isalpha():
            count += 1
    
    return count