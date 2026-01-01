def bad_character_heuristic(self):
    """
        Encuentra todas las ocurrencias del patrón en el texto.
        :return: Una lista de todas las posiciones del patrón en el texto, lista.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]
        """
    positions = []
    currentPos = 0
    while currentPos <= self.textLen - self.patLen:
        mismatchPos = self.mismatch_in_text(currentPos)
        if mismatchPos == -1:
            positions.append(currentPos)
            currentPos += 1
        else:
            badCharIndex = self.match_in_pattern(self.text[mismatchPos])
            shift = mismatchPos - (currentPos + badCharIndex)
            currentPos += max(1, shift)
    return positions