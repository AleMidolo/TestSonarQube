def split_sentences(self, text):
    """
    将文本分割成一个句子列表，除了最后一个句子外不带标点符号
    :param text: 要分割的文本
    :return: 分割后的文本列表
    >>> ru = RegexUtils()
    >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
    ['Aaa', 'Bbbb', 'Ccc!']
    """
    import re
    
    # 按句子结束标点符号分割
    sentences = re.split(r'([.!?]+)', text)
    
    # 过滤空字符串并去除空白
    result = []
    i = 0
    while i < len(sentences):
        sentence = sentences[i].strip()
        if sentence:
            # 如果是最后一个非空句子，保留标点
            if i + 1 < len(sentences) and sentences[i + 1].strip() in ['.', '!', '?', '..', '!!', '??']:
                # 对于非最后的句子，不添加标点
                if i + 2 < len(sentences) and any(sentences[j].strip() for j in range(i + 2, len(sentences))):
                    result.append(sentence)
                    i += 2
                else:
                    # 这是最后一个句子，保留标点
                    result.append(sentence + sentences[i + 1].strip())
                    i += 2
            else:
                result.append(sentence)
                i += 1
        else:
            i += 1
    
    return result