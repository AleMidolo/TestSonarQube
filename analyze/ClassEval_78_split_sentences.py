def split_sentences(self, sentences_string):
    """
        Divide una cadena en una lista de oraciones. Las oraciones terminan con . o ? y con un espacio después de eso. Tenga en cuenta que Sr. también termina con . pero no son oraciones.
        :param sentences_string: string, cadena a dividir
        :return:list, lista de oraciones divididas
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!Sr)(?<!Sra)(?<!Dr)(?<!Prof)\\.\\s+|\\?\\s+'
    parts = re.split(f'({pattern})', sentences_string)
    sentences = []
    current_sentence = ''
    for i in range(0, len(parts), 2):
        if i < len(parts):
            current_sentence += parts[i]
            if i + 1 < len(parts):
                delimiter = parts[i + 1].strip()
                current_sentence += delimiter
                sentences.append(current_sentence.strip())
                current_sentence = ''
    if current_sentence:
        sentences.append(current_sentence.strip())
    sentences = [s for s in sentences if s]
    return sentences