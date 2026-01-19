def split_sentences(self, sentences_string):
    """
        Suddivide una stringa in una lista di frasi. Le frasi terminano con . o ? e con uno spazio dopo. Si prega di notare che Mr. termina anch'esso con . ma non è una frase.
        :param sentences_string: stringa, stringa da suddividere
        :return: lista, lista delle frasi suddivise
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    if not sentences_string:
        return []
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bMs)(?<!\\bDr)(?<!\\bProf)(?<!\\bSr)(?<!\\bJr)\\.\\s+|\\?\\s+'
    parts = re.split(pattern, sentences_string)
    sentences = []
    for i in range(len(parts) - 1):
        delimiter_match = re.search(pattern, sentences_string)
        if delimiter_match:
            if '.' in delimiter_match.group():
                sentences.append(parts[i] + '.')
            else:
                sentences.append(parts[i] + '?')
            sentences_string = sentences_string[len(parts[i]) + len(delimiter_match.group()):]
    if parts[-1]:
        if parts[-1].endswith('.') or parts[-1].endswith('?'):
            sentences.append(parts[-1])
        else:
            pass
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences