def split_sentences(self, sentences_string):
    """
    将字符串拆分为句子列表。句子以 . 或 ? 结尾，并且后面有一个空格。请注意，Mr. 也以 . 结尾，但不是句子。
    :param sentences_string: 字符串, 要拆分的字符串
    :return:list, 拆分后的句子列表
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    import re
    
    # 使用正则表达式匹配句子
    # 匹配以 . 或 ? 结尾且后面跟空格的模式，但排除 Mr. 这种情况
    # 负向前瞻确保 . 前面不是 Mr
    # 使用 (?<!Mr)\. 来排除 Mr. 的情况
    pattern = r'(?<!Mr)[.?](?=\s|$)'
    
    # 先找到所有分割点
    sentences = []
    last_end = 0
    
    for match in re.finditer(pattern, sentences_string):
        end_pos = match.end()
        sentence = sentences_string[last_end:end_pos].strip()
        if sentence:
            sentences.append(sentence)
        last_end = end_pos
    
    # 处理最后一个句子（如果没有以空格结尾）
    if last_end < len(sentences_string):
        last_sentence = sentences_string[last_end:].strip()
        if last_sentence:
            sentences.append(last_sentence)
    
    return sentences