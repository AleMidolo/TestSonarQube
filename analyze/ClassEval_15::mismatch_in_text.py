def mismatch_in_text(self, currentPos):
    """
        Determina la posición de la primera discrepancia entre el patrón y el texto.
        :param currentPos: La posición actual en el texto, int.
        :return: La posición de la primera discrepancia entre el patrón y el texto, int, de lo contrario -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2
        """
    for j in range(self.patLen - 1, -1, -1):
        if currentPos + j >= self.textLen or self.text[currentPos + j] != self.pattern[j]:
            return j
    return -1