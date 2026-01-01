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
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bDr)(?<!\\bMs)(?<!\\bProf)\\.\\s|\\?\\s'
    sentences = re.split(pattern, sentences_string)
    result = []
    for i in range(len(sentences)):
        if i < len(sentences) - 1:
            match = re.search('[.?]\\s' + re.escape(sentences[i + 1].split()[0] if sentences[i + 1].split() else ''), sentences_string[len(''.join(result)):] if result else sentences_string)
            if match:
                punctuation = match.group()[0]
                result.append(sentences[i].strip() + punctuation)
            else:
                result.append(sentences[i].strip())
        elif sentences[i].strip():
            result.append(sentences[i].strip())
    result = [s for s in result if s]
    return result