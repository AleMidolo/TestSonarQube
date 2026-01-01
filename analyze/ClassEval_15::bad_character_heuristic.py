def bad_character_heuristic(self):
    """
        Encuentra todas las ocurrencias del patrón en el texto.
        :return: Una lista de todas las posiciones del patrón en el texto, lista.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]

        """
    if self.patLen == 0:
        return []
    positions = []
    current_pos = 0
    while current_pos <= self.textLen - self.patLen:
        mismatch_pos = self.mismatch_in_text(current_pos)
        if mismatch_pos == -1:
            positions.append(current_pos)
            current_pos += self.patLen
        else:
            bad_char = self.text[mismatch_pos]
            rightmost_pos = self.match_in_pattern(bad_char)
            if rightmost_pos == -1:
                current_pos = mismatch_pos + 1
            else:
                pattern_pos = mismatch_pos - current_pos
                shift = pattern_pos - rightmost_pos
                current_pos += max(1, shift)
    return positions