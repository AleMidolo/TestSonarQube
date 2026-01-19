def bad_character_heuristic(self):
    """
        Encuentra todas las ocurrencias del patrón en el texto.
        :return: Una lista de todas las posiciones del patrón en el texto, lista.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]
        """
    positions = []
    skip = 0
    while skip <= self.textLen - self.patLen:
        mismatch_index = self.mismatch_in_text(skip)
        if mismatch_index == -1:
            positions.append(skip)
            skip += self.patLen - self.match_in_pattern(self.text[skip + self.patLen - 1]) if skip + self.patLen < self.textLen else 1
        else:
            skip += max(1, mismatch_index - skip - self.match_in_pattern(self.text[mismatch_index]))
    return positions