def is_valid_input(self, textnum):
    """
        Controlla se il testo di input contiene solo parole valide che possono essere convertite in numeri.
        :param textnum: Il testo di input contenente parole che rappresentano numeri.
        :return: True se l'input è valido, False altrimenti.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    valid_words = set(self.numwords.keys()).union(set(self.ordinal_words.keys()))
    words = textnum.replace('-', ' ').split()
    return all((word in valid_words for word in words))