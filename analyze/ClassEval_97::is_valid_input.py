def is_valid_input(self, textnum):
    """
        Controlla se il testo di input contiene solo parole valide che possono essere convertite in numeri.
        :param textnum: Il testo di input contenente parole che rappresentano numeri.
        :return: True se l'input è valido, False altrimenti.
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
        is_ordinal = False
        for ending, replacement in self.ordinal_endings:
            if word.endswith(ending):
                base_word = word[:-len(ending)] + replacement
                if base_word in self.numwords:
                    is_ordinal = True
                    break
        if is_ordinal:
            continue
        if word not in self.numwords:
            return False
    return True