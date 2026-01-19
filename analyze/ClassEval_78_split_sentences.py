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
    pattern = r'(?<!Mr)[\.\?](?=\s|$)'
    
    # 先按模式分割
    parts = re.split(pattern, sentences_string)
    
    # 重新组合句子，添加回分隔符
    sentences = []
    matches = re.finditer(pattern, sentences_string)
    match_positions = [(m.start(), m.group()) for m in matches]
    
    if not match_positions:
        return [sentences_string.strip()] if sentences_string.strip() else []
    
    start = 0
    for i, (pos, delimiter) in enumerate(match_positions):
        sentence = sentences_string[start:pos + 1].strip()
        if sentence:
            sentences.append(sentence)
        start = pos + 1
    
    # 处理最后剩余的部分
    if start < len(sentences_string):
        remaining = sentences_string[start:].strip()
        if remaining:
            sentences.append(remaining)
    
    return sentences