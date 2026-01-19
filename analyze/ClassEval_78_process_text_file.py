def process_text_file(self, sentences_string):
    """
    给定一段文本，返回最长句子中的单词数量
    :param sentences_string: 字符串，未分割的长句子
    :return: int，最长句子中的单词数量
    >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
    4
    """
    import re
    
    # 按照句子分隔符（. ? !）分割文本
    sentences = re.split(r'[.?!]+', sentences_string)
    
    max_word_count = 0
    
    for sentence in sentences:
        # 去除首尾空格并分割单词
        words = sentence.strip().split()
        # 更新最大单词数
        max_word_count = max(max_word_count, len(words))
    
    return max_word_count