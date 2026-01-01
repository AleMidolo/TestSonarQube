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
    return [sentence.strip() for sentence in sentences if sentence]