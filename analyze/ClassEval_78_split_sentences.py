def split_sentences(self, sentences_string):
    """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bMs)(?<!\\bDr)(?<!\\bProf)(?<!\\bRev)(?<!\\bSt)\\.\\s|\\?\\s'
    parts = re.split(pattern, sentences_string)
    sentences = []
    for i in range(len(parts) - 1):
        if re.search('(?<!\\bMr)(?<!\\bMrs)(?<!\\bMs)(?<!\\bDr)(?<!\\bProf)(?<!\\bRev)(?<!\\bSt)\\.\\s', parts[i] + '. '):
            sentences.append(parts[i] + '.')
        else:
            sentences.append(parts[i] + '?')
    if parts[-1].strip():
        sentences.append(parts[-1])
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences