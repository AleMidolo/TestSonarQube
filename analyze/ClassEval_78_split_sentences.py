def split_sentences(self, sentences_string):
    """
        将字符串拆分为句子列表。句子以 . 或 ? 结尾，并且后面有一个空格。请注意，Mr. 也以 . 结尾，但不是句子。
        :param sentences_string: 字符串, 要拆分的字符串
        :return:list, 拆分后的句子列表
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!Mr)([.?])\\s+'
    parts = re.split(pattern, sentences_string)
    sentences = []
    i = 0
    while i < len(parts):
        if i + 1 < len(parts):
            sentences.append(parts[i] + parts[i + 1])
            i += 2
        else:
            if parts[i].strip():
                sentences.append(parts[i])
            i += 1
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences