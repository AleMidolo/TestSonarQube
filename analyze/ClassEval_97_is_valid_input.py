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
    for word in words:
        if word not in self.numwords and word not in self.ordinal_words:
            return False
    return True