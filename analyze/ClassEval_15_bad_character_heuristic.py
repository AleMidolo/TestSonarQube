def bad_character_heuristic(self):
    """
        Trova tutte le occorrenze del pattern nel testo.
        :return: Una lista di tutte le posizioni del modello nel testo, lista.
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
            shift = max(1, mismatchPos - (currentPos + badCharIndex))
            currentPos += shift
    return positions