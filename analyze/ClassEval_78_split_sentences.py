def split_sentences(self, sentences_string):
    """
        Divide una cadena en una lista de oraciones. Las oraciones terminan con . o ? y con un espacio después de eso. Tenga en cuenta que Sr. también termina con . pero no son oraciones.
        :param sentences_string: string, cadena a dividir
        :return:list, lista de oraciones divididas
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    pattern = '(?<!Sr)(?<!Sra)(?<!Dr)(?<!Prof)(?<!Mr)(?<!Mrs)(?<!Ms)(?<!St)\\.\\s|\\?\\s'
    parts = re.split(f'({pattern})', sentences_string)
    sentences = []
    current_sentence = ''
    for i in range(0, len(parts) - 1, 2):
        if i + 1 < len(parts):
            current_sentence = parts[i] + parts[i + 1].rstrip()
            sentences.append(current_sentence.strip())
    if len(parts) % 2 == 1:
        last_part = parts[-1].strip()
        if last_part:
            sentences.append(last_part)
    sentences = [s for s in sentences if s]
    return sentences