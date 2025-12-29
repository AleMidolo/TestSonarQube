def split_sentences(self, sentences_string):
    """
        Suddivide una stringa in una lista di frasi. Le frasi terminano con . o ? e con uno spazio dopo. Si prega di notare che Mr. termina anch'esso con . ma non è una frase.
        :param sentences_string: stringa, stringa da suddividere
        :return: lista, lista delle frasi suddivise
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)\\.\\s+|\\?\\s+'
    parts = re.split(pattern, sentences_string)
    sentences = []
    for i, part in enumerate(parts):
        if i < len(parts) - 1:
            match = re.search(pattern, sentences_string)
            if match:
                delimiter = match.group(0).strip()
                sentences.append(part + delimiter)
                sentences_string = sentences_string[match.end():]
    if parts[-1] and (parts[-1].endswith('.') or parts[-1].endswith('?')):
        sentences.append(parts[-1])
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences