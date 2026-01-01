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
    sentences = re.split(pattern, sentences_string)
    sentences = [s.strip() for s in sentences if s.strip()]
    result = []
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            next_start = sentences_string.find(sentences[i + 1]) if i + 1 < len(sentences) else len(sentences_string)
            current_end = sentences_string.find(sentences[i]) + len(sentences[i])
            if current_end < next_start:
                punctuation = sentences_string[current_end:next_start].strip()
                if punctuation and punctuation[0] in '.?':
                    result.append(sentence + punctuation[0])
                else:
                    result.append(sentence)
            else:
                result.append(sentence)
        elif sentences_string.strip().endswith(sentence):
            start_idx = sentences_string.rfind(sentence)
            if start_idx != -1:
                end_idx = start_idx + len(sentence)
                if end_idx < len(sentences_string) and sentences_string[end_idx] in '.?':
                    result.append(sentence + sentences_string[end_idx])
                else:
                    result.append(sentence)
            else:
                result.append(sentence)
        else:
            result.append(sentence)
    return result