def split_sentences(self, text):
    """
    将文本分割成一个句子列表，除了最后一个句子外不带标点符号
    :param text: 要分割的文本
    :return: 分割后的文本列表
    >>> ru = RegexUtils()
    >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
    ['Aaa', 'Bbbb', 'Ccc!']
    """
    if not text:
        return []

    # 使用正则表达式按句子结束标点符号分割
    # 匹配句子结束符号（. ? !）后面跟着空格或字符串结束
    sentences = re.split(r'([.?!])\s+', text)

    result = []
    i = 0

    # 处理分割后的列表
    while i < len(sentences):
        if sentences[i]:  # 跳过空字符串
            # 如果是句子内容
            if i + 1 < len(sentences) and sentences[i + 1] in '.?!':
                # 当前是句子内容，下一个是标点
                result.append(sentences[i])
                i += 2
            elif i == len(sentences) - 1:
                # 最后一个元素，保留标点
                result.append(sentences[i])
                i += 1
            else:
                result.append(sentences[i])
                i += 1
        else:
            i += 1

    return result