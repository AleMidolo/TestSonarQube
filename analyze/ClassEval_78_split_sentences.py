def split_sentences(self, sentences_string):
    """
        Divide una cadena en una lista de oraciones. Las oraciones terminan con . o ? y con un espacio después de eso. Tenga en cuenta que Sr. también termina con . pero no son oraciones.
        :param sentences_string: string, cadena a dividir
        :return:list, lista de oraciones divididas
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    sentences = re.split('(?<!\\bSr)\\. |\\? ', sentences_string)
    return [sentence.strip() for sentence in sentences if sentence.strip()]