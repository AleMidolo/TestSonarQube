def split_sentences(self, sentences_string):
    """
        将字符串拆分为句子列表。句子以 . 或 ? 结尾，并且后面有一个空格。请注意，Mr. 也以 . 结尾，但不是句子。
        :param sentences_string: 字符串, 要拆分的字符串
        :return:list, 拆分后的句子列表
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)\\.\\s+|\\?\\s+'
    sentences = re.split(pattern, sentences_string)
    result = []
    matches = list(re.finditer(pattern, sentences_string))
    for i, sentence in enumerate(sentences):
        if i < len(matches):
            punct = matches[i].group().strip()
            result.append(sentence + punct)
        elif sentence.strip():
            result.append(sentence.strip())
    result = [s.strip() for s in result if s.strip()]
    return result