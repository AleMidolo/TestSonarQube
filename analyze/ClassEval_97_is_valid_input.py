def is_valid_input(self, textnum):
    """
        Controlla se il testo di input contiene solo parole valide che possono essere convertite in numeri.
        :param textnum: Il testo di input contenente parole che rappresentano numeri.
        :return: True se l'input è valido, False altrimenti.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    words = textnum.replace('-', ' ').split()
    return all((word in self.numwords or word in self.ordinal_words for word in words))