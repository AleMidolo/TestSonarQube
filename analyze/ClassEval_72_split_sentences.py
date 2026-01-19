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

    while i < len(sentences):
        if sentences[i]:  # 跳过空字符串
            # 如果这是最后一个非空元素
            if i == len(sentences) - 1:
                result.append(sentences[i])
            # 如果下一个元素是标点符号
            elif i + 1 < len(sentences) and sentences[i + 1] in '.?!':
                # 对于非最后的句子，只保留文本部分，不加标点
                result.append(sentences[i])
                i += 1  # 跳过标点符号
            else:
                result.append(sentences[i])
        i += 1

    return result