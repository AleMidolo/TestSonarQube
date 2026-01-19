def split_sentences(self, sentences_string):
    """
        Divide una cadena en una lista de oraciones. Las oraciones terminan con . o ? y con un espacio después de eso. Tenga en cuenta que Sr. también termina con . pero no son oraciones.
        :param sentences_string: string, cadena a dividir
        :return:list, lista de oraciones divididas
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!Sr)(?<!Sra)(?<!Dr)(?<!Prof)(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Jr)\\.\\s+|\\?\\s+'
    parts = re.split(pattern, sentences_string)
    sentences = []
    for i in range(len(parts)):
        if i < len(parts) - 1:
            match = re.search(pattern, sentences_string)
            if match:
                delimiter = match.group(0).strip()
                sentences.append(parts[i] + delimiter[:-1])
                sentences_string = sentences_string[match.end():]
    if parts[-1].strip():
        last_part = parts[-1].strip()
        if last_part.endswith('.') or last_part.endswith('?'):
            sentences.append(last_part)
    return sentences