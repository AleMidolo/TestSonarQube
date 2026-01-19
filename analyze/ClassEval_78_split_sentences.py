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
            # 检查是否后面有空格（或者是字符串末尾）
            if i + 1 < len(sentences_string) and sentences_string[i + 1] == ' ':
                # 检查是否是 Mr. 的情况
                # Mr. 的特征：. 前面是 Mr
                if sentences_string[i] == '.':
                    # 检查当前句子是否以 Mr. 结尾
                    if len(current_sentence) >= 3 and current_sentence[-3:] == 'Mr.':
                        i += 1
                        continue
                
                # 这是一个句子的结束
                sentences.append(current_sentence.strip())
                current_sentence = ""
                i += 1  # 跳过空格
                continue
            elif i + 1 == len(sentences_string):
                # 字符串末尾
                sentences.append(current_sentence.strip())
                current_sentence = ""
        
        i += 1
    
    # 如果还有剩余内容
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    
    return sentences