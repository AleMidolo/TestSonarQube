def split_sentences(self, sentences_string):
    """
        Suddivide una stringa in una lista di frasi. Le frasi terminano con . o ? e con uno spazio dopo. Si prega di notare che Mr. termina anch'esso con . ma non è una frase.
        :param sentences_string: stringa, stringa da suddividere
        :return: lista, lista delle frasi suddivise
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!\\bMr)(?<!\\bMrs)(?<!\\bMs)(?<!\\bDr)(?<!\\bProf)(?<!\\bRev)(?<!\\bHon)\\.\\s+|\\?\\s+'
    sentences = re.split(pattern, sentences_string)
    sentences = [s.strip() for s in sentences if s.strip()]
    result = []
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            start_pos = sentences_string.find(sentence)
            if start_pos != -1:
                end_pos = start_pos + len(sentence)
                if end_pos < len(sentences_string):
                    if sentences_string[end_pos:end_pos + 2] == '. ':
                        result.append(sentence + '.')
                    elif sentences_string[end_pos:end_pos + 2] == '? ':
                        result.append(sentence + '?')
                    else:
                        result.append(sentence)
        elif sentence and (sentence.endswith('.') or sentence.endswith('?')):
            result.append(sentence)
        elif sentences_string.strip().endswith(('.', '?')):
            last_dot = sentences_string.rfind('.')
            last_question = sentences_string.rfind('?')
            last_punct = max(last_dot, last_question)
            if last_punct != -1:
                result.append(sentences_string[:last_punct + 1].strip())
            else:
                result.append(sentence)
        else:
            result.append(sentence)
    return result