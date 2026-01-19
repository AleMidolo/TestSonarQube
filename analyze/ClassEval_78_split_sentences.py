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
    match_list = list(matches)
    
    if not match_list:
        return [sentences_string.strip()] if sentences_string.strip() else []
    
    # 使用另一种方法：找到所有分割点
    split_positions = []
    i = 0
    while i < len(sentences_string):
        if sentences_string[i] in '.?':
            # 检查是否是 Mr.
            if sentences_string[i] == '.' and i >= 2 and sentences_string[i-2:i] == 'Mr':
                i += 1
                continue
            # 检查后面是否有空格或是字符串末尾
            if i + 1 < len(sentences_string) and sentences_string[i + 1] == ' ':
                split_positions.append(i + 1)
            elif i + 1 == len(sentences_string):
                split_positions.append(i + 1)
        i += 1
    
    # 根据分割位置提取句子
    start = 0
    for pos in split_positions:
        sentence = sentences_string[start:pos].strip()
        if sentence:
            sentences.append(sentence)
        start = pos
    
    return sentences