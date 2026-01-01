def split_sentences(self, sentences_string):
    """
        将字符串拆分为句子列表。句子以 . 或 ? 结尾，并且后面有一个空格。请注意，Mr. 也以 . 结尾，但不是句子。
        :param sentences_string: 字符串, 要拆分的字符串
        :return:list, 拆分后的句子列表
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    return re.split('(?<=[.?\\s])\\s*', sentences_string.strip())