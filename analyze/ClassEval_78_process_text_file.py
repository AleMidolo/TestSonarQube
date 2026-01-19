def process_text_file(self, sentences_string):
    """
    给定一段文本，返回最长句子中的单词数量
    :param sentences_string: 字符串，未分割的长句子
    :return: int，最长句子中的单词数量
    >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
    4
    """
    import re
    
    # Split the text into sentences using punctuation marks (. ? !)
    sentences = re.split(r'[.?!]', sentences_string)
    
    max_word_count = 0
    
    for sentence in sentences:
        # Strip whitespace and split by spaces to get words
        words = sentence.strip().split()
        # Count non-empty words
        word_count = len([word for word in words if word])
        max_word_count = max(max_word_count, word_count)
    
    return max_word_count