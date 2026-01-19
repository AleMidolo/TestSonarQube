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
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bDr)(?<!\\bMs)(?<!\\bProf)\\.|\\?(?=\\s|$)'
    matches = list(re.finditer(pattern, sentences_string))
    if not matches:
        return [sentences_string.strip()]
    sentences = []
    start = 0
    for match in matches:
        end = match.end()
        sentence = sentences_string[start:end].strip()
        if sentence:
            sentences.append(sentence)
        start = end
    if start < len(sentences_string):
        remaining = sentences_string[start:].strip()
        if remaining:
            sentences.append(remaining)
    return sentences