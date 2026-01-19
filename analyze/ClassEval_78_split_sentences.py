def split_sentences(self, sentences_string):
    """
    将字符串拆分为句子列表。句子以 . 或 ? 结尾，并且后面有一个空格。请注意，Mr. 也以 . 结尾，但不是句子。
    :param sentences_string: 字符串, 要拆分的字符串
    :return:list, 拆分后的句子列表
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    if not sentences_string:
        return []
    
    sentences = []
    current_sentence = ""
    i = 0
    
    while i < len(sentences_string):
        current_sentence += sentences_string[i]
        
        # 检查是否是句子结束符 (. 或 ?)
        if sentences_string[i] in '.?':
            # 检查是否是字符串末尾或后面跟着空格
            if i == len(sentences_string) - 1:
                # 字符串末尾，添加当前句子
                sentences.append(current_sentence.strip())
                current_sentence = ""
            elif i + 1 < len(sentences_string) and sentences_string[i + 1] == ' ':
                # 检查是否是 Mr. 的情况
                # Mr. 的特征：. 前面是 "Mr"
                if sentences_string[i] == '.' and current_sentence.strip().endswith('Mr.'):
                    # 这是 Mr.，不是句子结束，继续
                    i += 1
                    continue
                else:
                    # 这是句子结束
                    sentences.append(current_sentence.strip())
                    current_sentence = ""
                    # 跳过后面的空格
                    i += 1
                    while i < len(sentences_string) and sentences_string[i] == ' ':
                        i += 1
                    continue
        
        i += 1
    
    # 处理剩余的内容
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    
    return sentences