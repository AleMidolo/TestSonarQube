def bad_character_heuristic(self):
    """
        Trova tutte le occorrenze del pattern nel testo.
        :return: Una lista di tutte le posizioni del modello nel testo, lista.
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
            skip += 1
        else:
            char = self.text[mismatch_index]
            shift = self.match_in_pattern(char)
            if shift == -1:
                skip += mismatch_index + 1
            else:
                skip += mismatch_index - shift
    return positions