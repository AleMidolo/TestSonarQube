def bad_character_heuristic(self):
    """
        Trova tutte le occorrenze del pattern nel testo.
        :return: Una lista di tutte le posizioni del modello nel testo, lista.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]
        """
    positions = []
    shift = 0
    while shift <= self.textLen - self.patLen:
        mismatch_index = self.mismatch_in_text(shift)
        if mismatch_index == -1:
            positions.append(shift)
            shift += 1
        else:
            char = self.text[mismatch_index]
            bad_char_index = self.match_in_pattern(char)
            shift += max(1, mismatch_index - (shift + bad_char_index))
    return positions