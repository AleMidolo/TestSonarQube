def split_sentences(self, sentences_string):
    """
        Divide una cadena en una lista de oraciones. Las oraciones terminan con . o ? y con un espacio después de eso. Tenga en cuenta que Sr. también termina con . pero no son oraciones.
        :param sentences_string: string, cadena a dividir
        :return:list, lista de oraciones divididas
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!Sr)(?<!Sra)(?<!Dr)(?<!Prof)\\.|\\?(?=\\s|$)'
    parts = re.split(f'({pattern})', sentences_string)
    sentences = []
    current_sentence = ''
    i = 0
    while i < len(parts):
        current_sentence += parts[i]
        if i + 1 < len(parts) and re.match(pattern, parts[i + 1]):
            current_sentence += parts[i + 1]
            sentences.append(current_sentence.strip())
            current_sentence = ''
            i += 2
        else:
            i += 1
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    sentences = [s for s in sentences if s]
    return sentences