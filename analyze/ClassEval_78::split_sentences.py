def split_sentences(self, sentences_string):
    """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bMs)(?<!\\bDr)(?<!\\bProf)\\.\\s|\\?\\s'
    parts = re.split(pattern, sentences_string)
    sentences = []
    for i in range(len(parts) - 1):
        match = re.search(pattern, sentences_string)
        if match:
            start = 0
            for j in range(i):
                start += len(parts[j]) + len(re.search(pattern, sentences_string[start:]).group())
            punct_match = re.search(pattern, sentences_string[start:])
            if punct_match:
                punct = punct_match.group().strip()
                sentences.append(parts[i] + punct)
    if parts and parts[-1]:
        if re.search('[.?]$', parts[-1]):
            sentences.append(parts[-1])
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences