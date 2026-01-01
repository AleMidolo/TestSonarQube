def count_words(self, sentence):
    """
        Cuenta el número de palabras en una oración. Ten en cuenta que las palabras están separadas por espacios y que los signos de puntuación y los números no se cuentan como palabras.
        :param sentence:string, oración a contar, donde las palabras están separadas por espacios
        :return:int, número de palabras en la oración
        >>> ss.count_words("abc def")
        2
        """
    words = re.findall('\\b[a-zA-Z]+\\b', sentence)
    return len(words)