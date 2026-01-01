def bad_character_heuristic(self):
    """
        Trova tutte le occorrenze del pattern nel testo.
        :return: Una lista di tutte le posizioni del modello nel testo, lista.
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
            current_pos += 1
        else:
            bad_char = self.text[mismatch_pos]
            pattern_pos = self.match_in_pattern(bad_char)
            if pattern_pos == -1:
                current_pos = mismatch_pos + 1
            else:
                shift = mismatch_pos - (current_pos + pattern_pos)
                current_pos += max(1, shift)
    return positions