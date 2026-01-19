def is_valid_input(self, textnum):
    """
        Verifica si el texto de entrada contiene solo palabras válidas que se pueden convertir en números.
        :param textnum: El texto de entrada que contiene palabras que representan números.
        :return: True si la entrada es válida, False en caso contrario.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    valid_words = set(self.numwords.keys()).union(set(self.ordinal_words.keys()))
    words = textnum.replace('-', ' ').split()
    return all((word in valid_words for word in words))