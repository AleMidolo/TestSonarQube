def split_sentences(self, sentences_string):
    """
        Divide una cadena en una lista de oraciones. Las oraciones terminan con . o ? y con un espacio después de eso. Tenga en cuenta que Sr. también termina con . pero no son oraciones.
        :param sentences_string: string, cadena a dividir
        :return:list, lista de oraciones divididas
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!Sr)(?<!Sra)(?<!Dr)(?<!Prof)(?<!Mr)(?<!Mrs)(?<!Ms)\\.\\s|\\?\\s'
    sentences = re.split(pattern, sentences_string)
    sentences = [s.strip() for s in sentences if s.strip()]
    result = []
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            start_pos = len(''.join(sentences[:i + 1])) + i
            if start_pos < len(sentences_string):
                if sentences_string[start_pos] == '.':
                    result.append(sentence + '.')
                elif sentences_string[start_pos] == '?':
                    result.append(sentence + '?')
        elif sentences_string.strip().endswith(('.', '?')):
            if sentences_string.strip().endswith('.'):
                result.append(sentence + '.')
            elif sentences_string.strip().endswith('?'):
                result.append(sentence + '?')
        else:
            result.append(sentence)
    return result