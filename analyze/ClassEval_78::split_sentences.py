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
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bDr)(?<!\\bMs)(?<!\\bProf)(?<!\\bRev)(?<!\\bSt)\\.|\\?'
    sentences = []
    current_sentence = ''
    i = 0
    while i < len(sentences_string):
        char = sentences_string[i]
        current_sentence += char
        if char in ['.', '?']:
            if i == len(sentences_string) - 1 or sentences_string[i + 1] == ' ':
                if not self._is_abbreviation(current_sentence):
                    sentences.append(current_sentence.strip())
                    current_sentence = ''
                    if i + 1 < len(sentences_string) and sentences_string[i + 1] == ' ':
                        i += 1
        i += 1
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    return sentences