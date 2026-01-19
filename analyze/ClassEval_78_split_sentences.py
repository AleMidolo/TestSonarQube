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
    pattern = '(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Prof)(?<!Sr)(?<!Jr)\\.\\s|\\?\\s'
    parts = re.split(pattern, sentences_string)
    sentences = []
    for i in range(len(parts) - 1):
        end_match = re.search('[.?]\\s', sentences_string)
        if end_match:
            end_char = end_match.group()[0]
            sentences.append(parts[i].strip() + end_char)
            sentences_string = sentences_string[end_match.end():]
        else:
            sentences.append(parts[i].strip() + '.')
    if parts[-1].strip():
        if parts[-1].strip()[-1] in '.?':
            sentences.append(parts[-1].strip())
        else:
            sentences.append(parts[-1].strip() + '.')
    sentences = [s for s in sentences if s.strip()]
    return sentences