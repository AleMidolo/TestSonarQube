def mismatch_in_text(self, currentPos):
    """
        Determina la posición de la primera discrepancia entre el patrón y el texto.
        :param currentPos: La posición actual en el texto, int.
        :return: La posición de la primera discrepancia entre el patrón y el texto, int, de lo contrario -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2
        """
    for i in range(self.patLen):
        if currentPos + i >= self.textLen or self.text[currentPos + i] != self.pattern[i]:
            return i
    return -1