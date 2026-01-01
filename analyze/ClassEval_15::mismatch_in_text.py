def mismatch_in_text(self, currentPos):
    """
        Determina la posizione della prima discrepanza tra il pattern e il testo.
        :param currentPos: La posizione attuale nel testo, int.
        :return: La posizione della prima discrepanza tra il modello e il testo, int, altrimenti -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2
        """
    for i in range(self.patLen):
        if currentPos + i >= self.textLen or self.text[currentPos + i] != self.pattern[i]:
            return i
    return -1