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
    pattern = '(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Prof)\\.\\s+|\\?\\s+'
    sentences = re.split(pattern, sentences_string)
    sentences = [s.strip() for s in sentences if s.strip()]
    result = []
    matches = list(re.finditer(pattern, sentences_string))
    for i, sentence in enumerate(sentences):
        if i < len(matches):
            punct = matches[i].group().strip()
            result.append(sentence + punct)
        elif sentence and (sentence.endswith('.') or sentence.endswith('?')):
            result.append(sentence)
        else:
            result.append(sentence)
    return result