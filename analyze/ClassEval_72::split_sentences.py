def split_sentences(self, text):
    """
        Divide el texto en una lista de oraciones sin puntuación, excepto la última oración
        :param text: Texto a dividir
        :return: Lista de texto dividido
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """
    pattern = self.generate_split_sentences_pattern()
    sentences = re.split(pattern, text)
    result = []
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            result.append(sentence.rstrip('.!?'))
        else:
            result.append(sentence)
    return result