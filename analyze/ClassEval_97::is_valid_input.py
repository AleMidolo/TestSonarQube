def is_valid_input(self, textnum):
    """
        Verifica si el texto de entrada contiene solo palabras válidas que se pueden convertir en números.
        :param textnum: El texto de entrada que contiene palabras que representan números.
        :return: True si la entrada es válida, False en caso contrario.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    textnum = textnum.replace('-', ' ')
    words = textnum.split()
    if not words:
        return False
    for word in words:
        if word in self.ordinal_words:
            continue
        found_ordinal = False
        for ending, replacement in self.ordinal_endings:
            if word.endswith(ending):
                base_word = word[:-len(ending)] + replacement
                if base_word in self.numwords:
                    found_ordinal = True
                    break
        if found_ordinal:
            continue
        if word not in self.numwords:
            return False
    return True