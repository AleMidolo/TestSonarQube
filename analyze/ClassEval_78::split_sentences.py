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
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bMs)(?<!\\bDr)(?<!\\bProf)\\.\\s+|\\?\\s+'
    parts = re.split(pattern, sentences_string)
    sentences = []
    for i in range(len(parts)):
        if i < len(parts) - 1:
            match = re.search(pattern, sentences_string)
            if match:
                delimiter = match.group(0).strip()
                sentences.append(parts[i] + delimiter)
                sentences_string = sentences_string[len(parts[i] + match.group(0)):]
        elif parts[i].strip():
            if parts[i].endswith('.') or parts[i].endswith('?'):
                sentences.append(parts[i])
            else:
                sentences.append(parts[i])
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences