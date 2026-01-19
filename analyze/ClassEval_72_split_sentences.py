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
    
    # Split by sentence-ending punctuation (., ?, !)
    sentences = re.split(r'([.?!])', text)
    
    # Reconstruct sentences by pairing text with punctuation
    result = []
    i = 0
    while i < len(sentences):
        sentence = sentences[i].strip()
        if sentence:  # Skip empty strings
            # Check if there's a punctuation mark following
            if i + 1 < len(sentences) and sentences[i + 1] in '.?!':
                # Not the last sentence - don't include punctuation
                if i + 2 < len(sentences):
                    result.append(sentence)
                else:
                    # This is the last sentence - include punctuation
                    result.append(sentence + sentences[i + 1])
                i += 2
            else:
                result.append(sentence)
                i += 1
        else:
            i += 1
    
    return result