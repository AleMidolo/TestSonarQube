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
    pattern = '(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Prof)(?<!Sr)(?<!Jr)\\.\\s+|\\?\\s+'
    parts = re.split(pattern, sentences_string)
    sentences = []
    for i, part in enumerate(parts):
        if i < len(parts) - 1:
            match = re.search(pattern, sentences_string)
            if match:
                delimiter = match.group(0).strip()
                sentences.append(part + delimiter)
                sentences_string = sentences_string[len(part + match.group(0)):]
        elif part and (part.endswith('.') or part.endswith('?')):
            sentences.append(part)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences