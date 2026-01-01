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
    s = 0
    while s <= self.textLen - self.patLen:
        mismatch_pos = self.mismatch_in_text(s)
        if mismatch_pos == -1:
            positions.append(s)
            s += 1
        else:
            bad_char = self.text[mismatch_pos]
            bad_char_pos = self.match_in_pattern(bad_char)
            if bad_char_pos == -1:
                s = mismatch_pos + 1
            else:
                shift = mismatch_pos - (s + bad_char_pos)
                s += max(1, shift)
    return positions