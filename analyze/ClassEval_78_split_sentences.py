def split_sentences(self, sentences_string):
    """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    if not sentences_string:
        return []
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bMs)(?<!\\bDr)(?<!\\bProf)\\.\\s|\\?\\s'
    sentences = re.split(pattern, sentences_string)
    result = []
    for i in range(len(sentences)):
        if i < len(sentences) - 1:
            next_char = sentences_string[sentences_string.find(sentences[i]) + len(sentences[i])]
            if next_char == '.':
                result.append(sentences[i] + '.')
            elif next_char == '?':
                result.append(sentences[i] + '?')
        elif sentences[i].strip():
            result.append(sentences[i].strip())
    result = [s.strip() for s in result if s.strip()]
    return result